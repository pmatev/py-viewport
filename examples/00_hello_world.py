from viewport import Viewport
import numpy as np

with Viewport() as v:  # open async connection
    img = np.zeros([100,100,3], dtype=np.uint8)

    v.draw(img.tobytes())
