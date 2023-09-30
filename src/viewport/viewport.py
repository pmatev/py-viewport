import asyncio
import subprocess
from urllib.parse import urlparse, urlunparse
import tenacity
import websockets
import colorlog
import webbrowser

logger = colorlog.getLogger(__name__)
handler = colorlog.StreamHandler()
handler.setFormatter(
    colorlog.ColoredFormatter("%(log_color)s%(levelname)s:%(name)s:%(message)s")
)
logger.addHandler(handler)
logger.setLevel("INFO")


class Viewport:
    def __init__(self, uri="http://0.0.0.0:3000", open_browser=False) -> None:
        self.host_uri = urlparse(uri)
        self.websocket_uri = self.host_uri._replace(scheme="ws", path="/viewport")
        self.open_browser = open_browser
        self._server_proc = None

    async def __aenter__(self):
        if not await self._is_server_running():
            logger.warn(
                f"Viewport server not running yet. Starting server at {urlunparse(self.host_uri)}"
            )
            await self._start_server()

        try:
            await self._connect()
        except Exception as e:
            logger.exception(f"Error starting Viewport: {e}")
            await self.__aexit__(type(e), e, e.__traceback__)
            raise

        return self

    async def __aexit__(self, s, x, t):
        self._server_proc.terminate()
        await self._websocket.close()

    async def draw(self, img: bytes) -> None:
        await self._websocket.send(img)

    async def _is_server_running(self):
        logger.debug("Checking if server is running")
        try:
            async with websockets.connect(urlunparse(self.websocket_uri)):
                return True
        except ConnectionRefusedError:
            return False

    @tenacity.retry(stop=tenacity.stop_after_attempt(5), wait=tenacity.wait_fixed(1))
    async def _connect(self):
        logger.debug("Connecting to websocket server")
        self._websocket = await websockets.connect(urlunparse(self.websocket_uri))

    async def _start_server(self):
        self._server_proc = await asyncio.create_subprocess_exec(
            "uvicorn",
            "server:app",
            "--host",
            self.host_uri.hostname,
            "--port",
            str(self.host_uri.port),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        is_running = False
        while is_running is False:
            await asyncio.sleep(0.2)
            is_running = await self._is_server_running()

        logger.info("Viewport server started")
        if self.open_browser:
            webbrowser.open(urlunparse(self.host_uri))
