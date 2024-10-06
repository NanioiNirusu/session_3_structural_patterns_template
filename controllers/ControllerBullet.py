from models.Game import Game
from models.GameObject import GameObject
from models.enums.EnumGameObjectDirection import EnumGameObjectDirection


class ControllerBullet:

    @staticmethod
    def update(bullet: GameObject, game: Game, delta_time: float):
        # Check if the bullet's animation is currently animating
        if bullet.animation_is_animating:
            # Create a copy of the bullet's position
            position = list(bullet.position)

            # Update the bullet's position based on its direction and movement speed
            if bullet.direction == EnumGameObjectDirection.Up:
                position[1] -= bullet.movement_speed * delta_time
            elif bullet.direction == EnumGameObjectDirection.Down:
                position[1] += bullet.movement_speed * delta_time
            elif bullet.direction == EnumGameObjectDirection.Left:
                position[0] -= bullet.movement_speed * delta_time
            elif bullet.direction == EnumGameObjectDirection.Right:
                position[0] += bullet.movement_speed * delta_time

            # Initialize variables to track collision and the object to remove
            is_colliding = False
            other_object_remove = None

            # Check if the bullet is within the game map boundaries
            if 0 <= position[0] <= game.map_size[0] - 1 and 0 <= position[1] <= game.map_size[1] - 1:
                # Iterate over all game objects
                for other_object in game.game_objects:
                    # Skip the current bullet object
                    if other_object != bullet:
                        # Round the positions of the other object and the bullet to one decimal place
                        other_position_rounded = [round(other_object.position[0], 1),
                                                  round(other_object.position[1], 1)]
                        position_rounded = [round(position[0], 1), round(position[1], 1)]

                        # Define the rectangular boundaries of the bullet and the other object
                        rect_tank = [position_rounded[0], position_rounded[1], position_rounded[0] + 1,
                                     position_rounded[1] + 1]
                        rect_other_object = [other_position_rounded[0], other_position_rounded[1],
                                             other_position_rounded[0] + 1, other_position_rounded[1] + 1]

                        # Check if the bullet and the other object overlap
                        if rect_tank[0] < rect_other_object[2] and rect_tank[2] > rect_other_object[0] and rect_tank[
                            1] < rect_other_object[3] and rect_tank[3] > rect_other_object[1]:
                            # Set the collision flag to True
                            is_colliding = True
                            # Store the colliding object for removal
                            other_object_remove = other_object
                            # Exit the loop since a collision is found
                            break
            else:
                # Set the collision flag to True if the bullet is outside the game map boundaries
                is_colliding = True

            # Update the bullet's position if no collision occurred
            if not is_colliding:
                bullet.position = position
            else:
                # Remove the bullet from the game objects list
                game.game_objects.remove(bullet)
                # Remove the colliding object if one was found
                if other_object_remove is not None:
                    game.game_objects.remove(other_object_remove)
                    # Increase the game score by 1
                    game.score += 1