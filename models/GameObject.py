from dataclasses import dataclass, field
from typing import Tuple, List

from dataclasses_json import dataclass_json

from models.enums.EnumGameObjectDirection import EnumGameObjectDirection
from models.enums.EnumGameObjectType import EnumGameObjectType


@dataclass_json
@dataclass
class GameObject:
    # The position of the game object represented as a list of floats
    position: List[float] = field(default_factory=list)

    # The direction the game object is facing, using the EnumGameObjectDirection enum
    direction: EnumGameObjectDirection = EnumGameObjectDirection.NotSet

    # The type of the game object, using the EnumGameObjectType enum
    game_object_type: EnumGameObjectType = EnumGameObjectType.Tank

    # The level of the tank (assuming this is relevant for tank objects)
    tank_level: int = 0

    # The movement speed of the game object
    movement_speed: float = 1e-3

    # The next time the tank is allowed to move (assuming this is used for movement control)
    tank_next_move_time: float = 0

    # The current animation frame of the game object
    animation_frame: int = 0

    # The maximum number of animation frames for the game object
    animation_frame_max: int = 0

    # The duration of the current animation frame
    animation_frame_duration: float = 0

    # The maximum duration of an animation frame for the game object
    animation_frame_duration_max: float = 0

    # A boolean indicating whether the game object is currently animating
    animation_is_animating: bool = False

    # TODO: Implement the prototype pattern for cloning game objects
    def clone(self):
        # Convert the current game object to a JSON string representation
        json_obj = self.to_json(indent=4)

        # Create a new game object instance from the JSON string
        result = GameObject.from_json(json_obj)

        # Return the cloned game object
        return result