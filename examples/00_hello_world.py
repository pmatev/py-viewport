from viewport import Viewport
import numpy as np


async def test_viewport():
    async with Viewport() as v:  # open async connection
        img = np.zeros([100, 100, 3], dtype=np.uint8)

        await v.draw(img.tobytes())

        # keep the server running
        while True:
            await asyncio.sleep(0.1)


if __name__ == "__main__":
    import asyncio

    asyncio.run(test_viewport())
