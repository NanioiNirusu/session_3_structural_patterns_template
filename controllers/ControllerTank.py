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
        # Check if the tank's animation is currently animating
        if tank.animation_is_animating:
            # Create a copy of the tank's position list
            position = list(tank.position)

            # Update the tank's position based on its direction and movement speed
            if tank.direction == EnumGameObjectDirection.Up:
                position[1] -= tank.movement_speed * delta_time
            elif tank.direction == EnumGameObjectDirection.Down:
                position[1] += tank.movement_speed * delta_time
            elif tank.direction == EnumGameObjectDirection.Left:
                position[0] -= tank.movement_speed * delta_time
            elif tank.direction == EnumGameObjectDirection.Right:
                position[0] += tank.movement_speed * delta_time

            # Check if the tank is within the map bounds
            if 0 <= position[0] <= game.map_size[0] - 1 and 0 <= position[1] <= game.map_size[1] - 1:
                is_colliding = False

                # Check for collisions with other game objects
                for other_object in game.game_objects:
                    # Skip collision check if the other object is the tank itself or a bullet
                    if other_object != tank and other_object.game_object_type != EnumGameObjectType.Bullet:
                        # Round the positions to one decimal place for collision detection
                        other_position_rounded = [round(other_object.position[0], 1),
                                                  round(other_object.position[1], 1)]
                        position_rounded = [round(position[0], 1), round(position[1], 1)]

                        # Create rectangles for the tank and other object
                        rect_tank = [position_rounded[0], position_rounded[1], position_rounded[0] + 1,
                                     position_rounded[1] + 1]
                        rect_other_object = [other_position_rounded[0], other_position_rounded[1],
                                             other_position_rounded[0] + 1, other_position_rounded[1] + 1]

                        # Check if the rectangles overlap (collision)
                        if rect_tank[0] < rect_other_object[2] and rect_tank[2] > rect_other_object[0] and rect_tank[
                            1] < rect_other_object[3] and rect_tank[3] > rect_other_object[1]:
                            is_colliding = True
                            break

                # Update the tank's position if no collision occurred
                if not is_colliding:
                    tank.position = position

    @staticmethod
    def fire(tank: GameObject, game: Game):
        # Create a new bullet object
        bullet = GameObject()

        # Set the bullet's initial position based on the tank's position
        bullet.position = [tank.position[0], tank.position[1]]

        # Set the bullet's direction to match the tank's direction
        bullet.direction = tank.direction

        # Adjust the bullet's position based on the tank's direction
        if tank.direction == EnumGameObjectDirection.Up:
            bullet.position[1] -= 1
        elif tank.direction == EnumGameObjectDirection.Down:
            bullet.position[1] += 1
        elif tank.direction == EnumGameObjectDirection.Left:
            bullet.position[0] -= 1
        elif tank.direction == EnumGameObjectDirection.Right:
            bullet.position[0] += 1

        # Set the bullet's movement speed
        bullet.movement_speed = 2e-3

        # Set the bullet's animation to be animating
        bullet.animation_is_animating = True

        # Set the bullet's game object type to Bullet
        bullet.game_object_type = EnumGameObjectType.Bullet

        # Add the bullet to the game's list of game objects
        game.game_objects.append(bullet)

    @staticmethod
    def set_direction(tank: GameObject, direction: EnumGameObjectDirection):
        # If the direction is NotSet, stop the tank's animation
        if direction == EnumGameObjectDirection.NotSet:
            tank.animation_is_animating = False
        else:
            # Set the tank's animation to be animating
            tank.animation_is_animating = True

            # Set the tank's direction to the specified direction
            tank.direction = direction

    @staticmethod
    def update_autonomous(tank: GameObject, game: Game, delta_time: float):
        # Check if it's time for a new action
        tank.tank_next_move_time -= delta_time
        if tank.tank_next_move_time <= 0:
            # Choose a new action
            ControllerTank.choose_new_action(tank, game)
            # Reset the timer (you can adjust this value)
            tank.tank_next_move_time = random.uniform(1000, 3000)  # 1-3 seconds

        # Move the tank based on its current direction
        ControllerTank.update(tank, game, delta_time)

    @staticmethod
    def choose_new_action(tank: GameObject, game: Game):
        # Randomly choose between moving and shooting
        if random.choice([True, False]):
            # Choose a random direction
            new_direction = random.choice(list(EnumGameObjectDirection))
            ControllerTank.set_direction(tank, new_direction)
        else:
            # Shoot
            ControllerTank.fire(tank, game)

