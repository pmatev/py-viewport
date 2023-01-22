import uvicorn
import numpy as np
import typer
import asyncio
from viewport import Viewport
from fastapi_websocket_pubsub import PubSubClient

cli = typer.Typer(name="py-viewport", no_args_is_help=True)

@cli.command()
def start(port: int = 3000, reload: bool = False):
    """Launch the viewport web server and web UI"""

    uvicorn.run('server:app', host='0.0.0.0', port=port, reload=reload)

@cli.command()
def test_draw():
    """Send a test websocket message"""

    async def _run_client():
        async with Viewport() as v:  # open async connection
            img = np.zeros([100,100,3], dtype=np.uint8)

            await v.draw(img.tobytes())

    loop = asyncio.new_event_loop()
    loop.run_until_complete(_run_client())

@cli.command()
def test_recv():
    """Listen for messages"""

    async def _print(data, topic):
        print('topic', len(data), type(data))

    async def _run_client():
        client = PubSubClient()
        client.subscribe('images', _print)
        client.start_client('ws://localhost:3000/ws')
        await client.wait_until_done()

    asyncio.run(_run_client())


if __name__ == "__main__":
    cli()