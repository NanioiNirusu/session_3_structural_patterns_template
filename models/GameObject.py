from dataclasses import dataclass, field
from typing import Tuple, List

from dataclasses_json import dataclass_json

from models.enums.EnumGameObjectDirection import EnumGameObjectDirection
from models.enums.EnumGameObjectType import EnumGameObjectType

@dataclass_json
@dataclass
class GameObject:
    position: List[float] = field(default_factory=list)
    direction: EnumGameObjectDirection = EnumGameObjectDirection.Up
    game_object_type: EnumGameObjectType = EnumGameObjectType.NotSet

    tank_level: int = 0
    movement_speed: float = 1e-3
    tank_next_move_time: float = 0

    animation_frame: int = 0
    animation_frame_max: int = 0
    animation_frame_duration: float = 0
    animation_frame_duration_max: float = 0
    animation_is_animating: bool = False

    # TODO prototype pattern
    def clone(self):
        json_obj = self.to_json(indent=4)
        result = GameObject.from_json(json_obj)
        return result