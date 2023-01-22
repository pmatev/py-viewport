import uvicorn
import numpy as np
import typer
from viewport import Viewport
from PIL import Image

cli = typer.Typer(name="py-viewport", no_args_is_help=True)


@cli.command()
def start(port: int = 3000, reload: bool = False):
    """Launch the viewport web server and web UI"""

    uvicorn.run('server:app', host='0.0.0.0', port=port, reload=reload)


@cli.command()
def draw():
    """Send a test websocket message - CLIENT PUBLISH"""

    with Viewport() as v:
        img = Image.open('test.jpg').resize((100, 100))
        img.putalpha(255)
        arr = np.array(img)

        v.draw(arr.tobytes())

        # rgb = np.array()
        # rgba = np.concatenate((rgb, np.zeros((100, 100, 1))), axis=2).shape
        # img = np.zeros([100,100,4], dtype=np.uint8)
        # img[]




if __name__ == "__main__":
    cli()