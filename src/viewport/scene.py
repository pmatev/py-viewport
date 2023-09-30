import json
from typing import List, Dict, Any, Union

from viewport.canvas2d import Canvas2D
from viewport.canvas3d import Canvas3D
from viewport.elements import Action, Element


class Scene:
    """
    A Scene consists of one or more Canvas elements.

    The Scene controls the rendering and layout concerns.
    All graphics elements happen within a Canvas.
    """

    def __init__(self) -> None:
        self.canvases: List[Union[Canvas2D, Canvas3D]] = []

    def to_json(self) -> List[Action]:
        actions: List[Action] = []
        for canvas in self.canvases:
            actions = actions + canvas.build()

        return actions

    def to_html(self) -> str:
        json_data = self.to_json()
        return f"""
            <script src="frontend/build/scene.js"></script>
            <div id="viewport-scene-root"></div>
            <script>
            window.__VIEWPORT__.DATA = {json.dumps(json_data)};
            window.__VIEWPORT__.run();
            </script>
        """

    def init_canvas_2d(self, width: int, height: int) -> Canvas2D:
        canvas = Canvas2D()
        self.canvases.append(canvas)
        return canvas

    def init_canvas_3d(self, width: int, height: int) -> Canvas3D:
        canvas = Canvas3D()
        self.canvases.append(canvas)
        return canvas
