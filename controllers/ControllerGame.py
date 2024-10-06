import random

from controllers.ControllerBullet import ControllerBullet
from controllers.ControllerTank import ControllerTank
from models.Game import Game
from models.GameObject import GameObject
from models.enums.EnumGameObjectType import EnumGameObjectType


class ControllerGame:
    __instance  = None

    def __init__(self):
        if ControllerGame.__instance is not None:
            raise Exception("Cannot create second instance of singleton")

        self._game: Game = None # non-static member variable
        ControllerGame.__instance = self

    @staticmethod
    def instance():
        if ControllerGame.__instance is None:
            ControllerGame() # new ControllerGame()
        return ControllerGame.__instance

    def player(self):
        game_object = None
        for game_object in self._game.game_objects:
            if game_object.game_object_type == EnumGameObjectType.Tank:
                break
        return game_object

    @property
    def game(self):
        return self._game

    def set_game(self, game):
        self._game = game

    def new_game(self):
        self._game = game = Game()

        # randomly choose map tile type
        game_object_options = [EnumGameObjectType.NotSet] * 30 + [
            EnumGameObjectType.Forest,
            EnumGameObjectType.Water,
            EnumGameObjectType.Brick,
            EnumGameObjectType.Steel,
            EnumGameObjectType.Enemy,
            EnumGameObjectType.Tank
        ]

        # prototype
        animated_game_object = GameObject()
        animated_game_object.animation_frame_duration = random.randint(0, int(animated_game_object.animation_frame_duration_max))
        animated_game_object.animation_frame_max = 2
        animated_game_object.animation_frame_duration_max = 500
        animated_game_object.animation_is_animating = True

        is_player_set = False
        for x in range(game.map_size[0]):
            for y in range(game.map_size[1]):
                game_object_type = random.choice(game_object_options)

                if game_object_type == EnumGameObjectType.Tank:
                    if not is_player_set:
                        is_player_set = True
                    else:
                        game_object_type = EnumGameObjectType.NotSet

                if game_object_type != EnumGameObjectType.NotSet:
                    game_object = animated_game_object.clone()
                    game_object.position = [x, y]
                    game_object.game_object_type = game_object_type

                    if game_object_type in [
                          EnumGameObjectType.Steel,EnumGameObjectType.Brick, EnumGameObjectType.Forest
]:
                        game_object.animation_is_animating = False

                    game.game_objects.append(game_object)


    def update(self, delta_time: float):
        game = self._game
        for game_object in game.game_objects:
            if game_object.game_object_type in [EnumGameObjectType.Tank, EnumGameObjectType.EnemyAdvanced, EnumGameObjectType.Enemy]:
                ControllerTank.update(game_object, game, delta_time)
            elif game_object.game_object_type == EnumGameObjectType.Bullet:
                ControllerBullet.update(game_object, game, delta_time)

            if game_object.animation_is_animating:
                game_object.animation_frame_duration += delta_time
                if game_object.animation_frame_duration >= game_object.animation_frame_duration_max:
                    game_object.animation_frame_duration = 0
                    game_object.animation_frame += 1
                    if game_object.animation_frame >= game_object.animation_frame_max:
                        game_object.animation_frame = 0
