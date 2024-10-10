from abc import ABC, abstractmethod
from models.Game import Game
import random
from models.GameObject import GameObject
from models.enums.EnumGameObjectType import EnumGameObjectType

# Abstract base class for building game levels
class LevelBuilder(ABC):


    class LevelBuilder(ABC):
        @abstractmethod
        def build_level(self, game: Game):
            print("Level0")
            pass

# Concrete class for building level 1 of the game
class Level1Builder(LevelBuilder):



    def build_level(self, game: Game):
        self.place_objects(game)
        # Add any other level-specific setup here
        print("Level1")

    def place_objects(self, game: Game):
        game_object_options = [EnumGameObjectType.NotSet] * 30 + [
            EnumGameObjectType.Forest,
            EnumGameObjectType.Water,
            EnumGameObjectType.Brick,
            EnumGameObjectType.Steel,
            EnumGameObjectType.Enemy,
            EnumGameObjectType.Tank
        ]

        animated_game_object = GameObject()
        animated_game_object.animation_frame_duration = random.randint(0,
                                                                       int(animated_game_object.animation_frame_duration_max))
        animated_game_object.animation_frame_max = 2
        animated_game_object.animation_frame_duration_max = 500
        animated_game_object.animation_is_animating = True

        is_player_set = False

        for x in range(game.map_size[0]):
            for y in range(game.map_size[1]):
                game_object_type = random.choice(game_object_options)

                if game_object_type != EnumGameObjectType.NotSet:
                    game_object = animated_game_object.clone()
                    game_object.position = [x, y]
                    game_object.game_object_type = game_object_type

                    if game_object_type == EnumGameObjectType.Tank:
                        if is_player_set:
                            game_object.game_object_type = EnumGameObjectType.Enemy
                        else:
                            is_player_set = True

                    if game_object_type in [EnumGameObjectType.Steel, EnumGameObjectType.Brick,
                                            EnumGameObjectType.Forest]:
                        game_object.animation_is_animating = False
                    elif game_object_type in [EnumGameObjectType.Enemy, EnumGameObjectType.EnemyAdvanced]:
                        game_object.tank_next_move_time = random.uniform(0, 2000)  # Start with a random time

                    game.game_objects.append(game_object)

        # # Ensure a player tank is created if it wasn't placed randomly
        # if not is_player_set:
        #     player_tank = animated_game_object.clone()
        #     player_tank.position = [random.randint(0, game.map_size[0] - 1), random.randint(0, game.map_size[1] - 1)]
        #     player_tank.game_object_type = EnumGameObjectType.Tank
        #     game.game_objects.append(player_tank)


# Concrete class for building level 2 of the game
class Level2Builder(LevelBuilder):


    def build_level(self, game: Game):
        print("Level2")
        self.place_objects(game)

        # Add any other level-specific setup here

    def place_objects(self, game: Game):
        game_object_options = [EnumGameObjectType.NotSet] * 30 + [
            EnumGameObjectType.Forest,
            EnumGameObjectType.Water,
            EnumGameObjectType.Brick,
            EnumGameObjectType.Steel,
            EnumGameObjectType.Enemy,
            EnumGameObjectType.Tank
        ]

        animated_game_object = GameObject()
        animated_game_object.animation_frame_duration = random.randint(0,
                                                                       int(animated_game_object.animation_frame_duration_max))
        animated_game_object.animation_frame_max = 2
        animated_game_object.animation_frame_duration_max = 500
        animated_game_object.animation_is_animating = True

        is_player_set = False

        for x in range(game.map_size[0]):
            for y in range(game.map_size[1]):
                game_object_type = random.choice(game_object_options)

                if game_object_type != EnumGameObjectType.NotSet:
                    game_object = animated_game_object.clone()
                    game_object.position = [x, y]
                    game_object.game_object_type = game_object_type

                    if game_object_type == EnumGameObjectType.Tank:
                        if is_player_set:
                            game_object.game_object_type = EnumGameObjectType.Enemy
                        else:
                            is_player_set = True

                    if game_object_type in [EnumGameObjectType.Steel, EnumGameObjectType.Brick,
                                            EnumGameObjectType.Forest]:
                        game_object.animation_is_animating = False
                    elif game_object_type in [EnumGameObjectType.Enemy, EnumGameObjectType.EnemyAdvanced]:
                        game_object.tank_next_move_time = random.uniform(0, 2000)  # Start with a random time

                    game.game_objects.append(game_object)

        # Ensure a player tank is created if it wasn't placed randomly
        # if not is_player_set:
        #     player_tank = animated_game_object.clone()
        #     player_tank.position = [random.randint(0, game.map_size[0] - 1), random.randint(0, game.map_size[1] - 1)]
        #     player_tank.game_object_type = EnumGameObjectType.Tank
        #     game.game_objects.append(player_tank)


