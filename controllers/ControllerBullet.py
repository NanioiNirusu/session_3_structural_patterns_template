from models.Game import Game
from models.GameObject import GameObject
from models.enums.EnumGameObjectDirection import EnumGameObjectDirection


class ControllerBullet:

    @staticmethod
    def update(bullet: GameObject, game: Game, delta_time: float):
        if bullet.animation_is_animating:
            position = list(bullet.position)
            if bullet.direction == EnumGameObjectDirection.Up:
                position[1] -= bullet.movement_speed * delta_time
            elif bullet.direction == EnumGameObjectDirection.Down:
                position[1] += bullet.movement_speed * delta_time
            elif bullet.direction == EnumGameObjectDirection.Left:
                position[0] -= bullet.movement_speed * delta_time
            elif bullet.direction == EnumGameObjectDirection.Right:
                position[0] += bullet.movement_speed * delta_time

            is_colliding = False
            other_object_remove = None

            if 0 <= position[0] <= game.map_size[0] - 1 and 0 <= position[1] <= game.map_size[1] - 1:
                for other_object in game.game_objects:
                    if other_object != bullet:
                        other_position_rounded = [round(other_object.position[0], 1), round(other_object.position[1], 1)]
                        position_rounded = [round(position[0], 1), round(position[1], 1)]
                        rect_tank = [position_rounded[0], position_rounded[1], position_rounded[0] + 1, position_rounded[1] + 1]
                        rect_other_object = [other_position_rounded[0], other_position_rounded[1], other_position_rounded[0] + 1, other_position_rounded[1] + 1]
                        # check overlap
                        if rect_tank[0] < rect_other_object[2] and rect_tank[2] > rect_other_object[0] and rect_tank[1] < rect_other_object[3] and rect_tank[3] > rect_other_object[1]:
                            is_colliding = True
                            other_object_remove = other_object
                            break
            else:
                is_colliding = True

            if not is_colliding:
                bullet.position = position
            else:
                game.game_objects.remove(bullet)
                if other_object_remove is not None:
                    game.game_objects.remove(other_object_remove)
                    game.score += 1