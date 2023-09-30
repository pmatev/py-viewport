import asyncio
import numpy as np
import pytest
from viewport import Viewport


@pytest.mark.asyncio
async def test_viewport():
    async with Viewport(open_browser=False) as v:
        img = np.zeros([100, 100, 3], dtype=np.uint8)
        await v.draw(img.tobytes())
