# py-viewport

A simple Python -> WebGL Bridge. Batteries not included.

Send raw image data to a browser window from python over websockets.

You can use this to live debug your python code and build visualisations without having to write out frames to a file or video.

## Getting started

Install
```sh
pip install py-viewport
```

Run the examples
```
python examples/00_hello_world.py
```

## Running in production
Start the server as a standalone process
```sh
py-viewport start
```

## Usage

Render an image to the viewport

```py
from viewport import Viewport

async with Viewport() as v:
    img = np.zeros([100,100,3], dtype=np.uint8)

    await v.draw(img.tobytes())
```


## Examples

- [examples/00_hello_world.py](examples/00_hello_world.py)
