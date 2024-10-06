import dataclasses
from dataclasses import field
from dataclasses import dataclass
from typing import List, Tuple

import dataclasses_json
from dataclasses_json import dataclass_json
from models.GameObject import GameObject


@dataclass_json
@dataclass
class Game:
    # Tuple representing the size of the game map (width, height)
    map_size: Tuple[int, int] = (20, 20)

    # List to store all the game objects present in the game
    # Uses the default_factory parameter to initialize an empty list
    game_objects: List[GameObject] = field(default_factory=list)

    # Integer representing the current level of the game
    level: int = 0

    # Integer representing the current score of the game
    score: int = 0