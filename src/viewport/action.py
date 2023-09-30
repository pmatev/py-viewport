from typing import List, Dict, Any

from viewport.elements import Element


class Canvas2D:
    """
    A 2D Canvas which can render itself and all children.

    A Canvas must always be used within a Scene to ensure correct interactivity and communication across modules.
    """

    width: int
    height: int

    def __init__(self) -> None:
        self.elements: List[Element] = []

    def build(self) -> List[Action]:
        return [
            {
                "action": "INIT_CANVAS",
                "data": {
                    "canvas_type": "2D",
                    "width": self.width,
                    "height": self.height,
                },
            }
        ]

    def to_json(self) -> List[Dict[str, Any]]:
        # enumerate actions to build up the visualisation
        return [{"type": el.type, "data": el.to_json()} for el in self.elements]
