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

## Development

Install system dependencies
```sh
brew install protobuf
```

Activate the python environment
```sh
pipenv install
pipenv shell
```

Install frontend dependencies and start the dev server
```sh
cd frontend/
npm install
```

Compile protobuf bindings
```sh
cd src/
./compile_protos.sh
```

Install the python package in editable mode
```sh
pip install -e .
```

Run the python server with live reload
```sh
py-viewport start --reload
```

Start the frontend dev server with live reload
```sh
cd frontend/
npm run start
```
