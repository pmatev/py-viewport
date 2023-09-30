from typing import List, Dict, Any

from viewport.elements import Action, Element


class Canvas3D:
    def __init__(self, width: int, height: int) -> None:
        self.elements: List[Element] = []
        self.width = width
        self.height = height

    def build(self) -> List[Action]:
        return [
            Action(
                action='INIT_CANVAS',
                data={
                    'canvas_type': '2D',
                    'width': self.width,
                    'height': self.height,
                }
            )
        ]

    def to_json(self) -> List[Dict[str, Any]]:
        return [
            {
                'type': el.type,
                'data': el.to_json()
            }
            for el in self.elements
        ]
