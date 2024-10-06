
import random
from pygame import Rect

from models.Game import Game
from models.GameObject import GameObject
from models.enums.EnumGameObjectDirection import EnumGameObjectDirection
from models.enums.EnumGameObjectType import EnumGameObjectType
from views.components.ComponentGameObject import sprite_width


class ControllerTank:

    @staticmethod
    def update(tank: GameObject, game: Game, delta_time: float):

        if tank.animation_is_animating:
            position = list(tank.position)
            if tank.direction == EnumGameObjectDirection.Up:
                position[1] -= tank.movement_speed * delta_time
            elif tank.direction == EnumGameObjectDirection.Down:
                position[1] += tank.movement_speed * delta_time
            elif tank.direction == EnumGameObjectDirection.Left:
                position[0] -= tank.movement_speed * delta_time
            elif tank.direction == EnumGameObjectDirection.Right:
                position[0] += tank.movement_speed * delta_time

            # if tank in map bounds
            if 0 <= position[0] <= game.map_size[0] - 1 and 0 <= position[1] <= game.map_size[1] - 1:
                is_colliding = False
                for other_object in game.game_objects:
                    if other_object != tank and other_object.game_object_type != EnumGameObjectType.Bullet:
                        other_position_rounded = [round(other_object.position[0], 1), round(other_object.position[1], 1)]
                        position_rounded = [round(position[0], 1), round(position[1], 1)]
                        rect_tank = [position_rounded[0], position_rounded[1], position_rounded[0] + 1, position_rounded[1] + 1]
                        rect_other_object = [other_position_rounded[0], other_position_rounded[1], other_position_rounded[0] + 1, other_position_rounded[1] + 1]
                        # check overlap
                        if rect_tank[0] < rect_other_object[2] and rect_tank[2] > rect_other_object[0] and rect_tank[1] < rect_other_object[3] and rect_tank[3] > rect_other_object[1]:
                            is_colliding = True
                            break

                if not is_colliding:
                    tank.position = position

    @staticmethod
    def fire(tank: GameObject, game: Game):
        bullet = GameObject()
        bullet.position = [tank.position[0], tank.position[1]]
        bullet.direction = tank.direction
        if tank.direction == EnumGameObjectDirection.Up:
            bullet.position[1] -= 1
        elif tank.direction == EnumGameObjectDirection.Down:
            bullet.position[1] += 1
        elif tank.direction == EnumGameObjectDirection.Left:
            bullet.position[0] -= 1
        elif tank.direction == EnumGameObjectDirection.Right:
            bullet.position[0] += 1
        bullet.movement_speed = 2e-3
        bullet.animation_is_animating = True
        bullet.game_object_type = EnumGameObjectType.Bullet
        game.game_objects.append(bullet)

    @staticmethod
    def set_direction(tank: GameObject, direction: EnumGameObjectDirection):
        if direction == EnumGameObjectDirection.NotSet:
            tank.animation_is_animating = False
        else:
            tank.animation_is_animating = True
            tank.direction = direction