from typing import Dict, Any, List
from dataclasses import dataclass
import numpy as np


@dataclass
class Action:
    action: str
    data: Dict[str, Any]


class Element:
    type: str = "Element"

    def build(self) -> List[Action]:
        return []

    def to_json(self) -> Dict[str, Any]:
        return {}


@dataclass
class FrameBuffer(Element):
    """
    Must match the width / height of the parent canvas
    """

    width: int
    height: int
    data: np.ndarray

    def build(self) -> List[Action]:
        return [Action(action="SET_FRAME_BUFFER", data=self.to_json())]

    def to_json(self) -> Dict[str, Any]:
        return {"width": self.width, "height": self.height, "data": self.data}
