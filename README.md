# py-viewport

A simple Python -> WebGL Bridge. Batteries not included.

Send raw image data to a browser window from python over websockets.

You can use this to live debug your python code and build visualisations without having to write out frames to a file or video.

## Getting started

Install
```sh
pip install py-viewport
```

Start the server
```sh
py-viewport start

# viewport is live on http://localhost:3000/
```

Render some data from python

```py
from viewport import Viewport
from PIL import Image

v = Viewport()  # defaults to 'http://localhost:3000/ws'

# support PIL images
with Image.open("./test.jpg") as img:
    v.draw(img)

# supports raw numpy image data
img = np.zeros([100,100,3],dtype=np.uint8)
v.draw(img)

```


## Examples

TODO