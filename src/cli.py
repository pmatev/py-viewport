import uvicorn
import numpy as np
import typer
from viewport import Viewport

cli = typer.Typer(name="py-viewport", no_args_is_help=True)


@cli.command()
def start(port: int = 3000, reload: bool = False):
    """Launch the viewport web server and web UI"""

    uvicorn.run('server:app', host='0.0.0.0', port=port, reload=reload)


@cli.command()
def draw():
    """Send a test websocket message - CLIENT PUBLISH"""

    with Viewport() as v:
        img = np.zeros([100,100,3], dtype=np.uint8)

        v.draw(img.tobytes())


if __name__ == "__main__":
    cli()