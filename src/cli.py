import uvicorn
import numpy as np
import typer
from PIL import Image

from viewport.scene import Scene
from viewport.viewport import Viewport


cli = typer.Typer(name="py-viewport", no_args_is_help=True)


@cli.command()
def start(port: int = 3000, reload: bool = False):
    """Launch the viewport web server and web UI"""

    uvicorn.run('server:app', host='0.0.0.0', port=port, reload=reload)


@cli.command()
def draw_ws():
    """Send a test websocket message - CLIENT PUBLISH"""

    with Viewport() as v:
        img = Image.open('test.jpg').resize((100, 100))
        img.putalpha(255)
        arr = np.array(img)

        v.draw(arr.tobytes())


@cli.command()
def draw_html():
    """Draw to static html"""

    scene = Scene()
    canvas = scene.init_canvas_2d(200, 200)

    img = Image.open('test.jpg').resize((200, 200))
    img.putalpha(255)

    canvas.set_pixels(np.array(img))
    canvas.add_image_layer('base', np.array(img))

    print(scene.to_html())


@cli.command()
def example_scene_with_run_api():
    """Full-featured streaming example"""

    scene = Scene()

    run = RunAPI('<run_id>')
    rgb = run.get_stream('cameras/front_forward')
    trajectory_overlay = get_trajectory_vis(run)
    model_predictions = get_model_predictions_vis(run)

    rgb_canvas = scene.init_canvas_2d('raw-canvas', 200, 200)
    rgb_canvas.register_stream(rgb)
    overlays_canvas = scene.init_canvas_2d('overlays-canvas', 200, 200)
    overlays_canvas.register_streams([trajectory_overlay, model_predictions])

    scene.use_layout('RAW + Overlays')  # use a saved layout

    # static embed can also register to running websocket server
    scene.to_html()

    '''
    open websocket
    read scene config and static injected data
    build the scene + canvas from the list of actions
    subscribe to registered streams
    data starts streaming in + buffer over timeline
    canvas updates
    -> user updates canvas widget (e.g. move slider)
        - update on frontend only?

    '''


if __name__ == "__main__":
    cli()
