from pathlib import Path
from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
import zmq
import zmq.asyncio
import logging

app = FastAPI()
context = zmq.asyncio.Context()
zmq_sock = context.socket(zmq.REP)

logger = logging.getLogger(__name__)

FRONTEND_DIR = Path(__file__).parent / 'frontend'


@app.on_event('startup')
def on_startup():
    zmq_sock.connect("tcp://127.0.0.1:11001")

app.mount("/static", StaticFiles(directory=FRONTEND_DIR / 'build/static', html=True), name="root")

@app.route("/")
async def index(arg):
    return FileResponse(FRONTEND_DIR / 'build/index.html')


@app.websocket("/viewport")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    while True:
        data = await zmq_sock.recv()

        if isinstance(data, bytes):
            logger.info('sending bytes')
            await websocket.send_bytes(data)

        # must reply to zmq socket to accept further requests
        await zmq_sock.send_string('ok')
