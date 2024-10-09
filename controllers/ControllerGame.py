import random

from controllers.ControllerBullet import ControllerBullet
from controllers.ControllerTank import ControllerTank
from models.Game import Game
from models.GameObject import GameObject
from models.enums.EnumGameObjectType import EnumGameObjectType
from models.Builders.LevelBuilder import Level1Builder, Level2Builder
import random

class ControllerGame:
    __instance = None

    def __init__(self):
        # Check if an instance of ControllerGame already exists
        # If it does, raise an exception to prevent creating a second instance (singleton pattern)
        if ControllerGame.__instance is not None:
            raise Exception("Cannot create second instance of singleton")

        # Initialize the _game member variable to None
        self._game: Game = None  # non-static member variable
        self.level_builders = [Level1Builder(), Level2Builder()]
        # Set the __instance class variable to the current instance
        ControllerGame.__instance = self

    @staticmethod
    def instance():
        # If no instance of ControllerGame exists, create one
        if ControllerGame.__instance is None:
            ControllerGame()  # new ControllerGame()

        # Return the singleton instance of ControllerGame
        return ControllerGame.__instance

    def player(self):

        # Initialize game_object to None
        game_object = None

        # Iterate through the game objects in the current game
        for game_object in self._game.game_objects:
            # If the game object is of type Tank, break the loop
            if game_object.game_object_type == EnumGameObjectType.Tank:
                break

        # Return the player game object (Tank)
        return game_object

    @property
    def game(self):
        # Getter method for the _game member variable
        return self._game

    def set_game(self, game):
        # Setter method for the _game member variable
        self._game = game

    def new_game(self):
        # Create a new Game instance and assign it to the _game member variable
        self._game = game = Game()
        # Randomly select a level builder from the list of available level builders
        chosen_builder = random.choice(self.level_builders)

        # Use the selected level builder to construct a level in the game instance
        chosen_builder.build_level(self._game)
        # Randomly choose map tile types
        # Create a list of game object types with weighted probabilities

        game_object_options = [EnumGameObjectType.NotSet] * 30 + [
            EnumGameObjectType.Forest,
            EnumGameObjectType.Water,
            EnumGameObjectType.Brick,
            EnumGameObjectType.Steel,
            EnumGameObjectType.Enemy,
            EnumGameObjectType.Tank,
        ]

        # Create a prototype GameObject instance for animation settings
        animated_game_object = GameObject()
        animated_game_object.animation_frame_duration = random.randint(0,
                                                                       int(animated_game_object.animation_frame_duration_max))
        animated_game_object.animation_frame_max = 2
        animated_game_object.animation_frame_duration_max = 500
        animated_game_object.animation_is_animating = True

        # Flag to track if the player's tank has been set
        # player_tank = animated_game_object.clone()
        # player_tank.position = [random.randint(0, game.map_size[0] - 1), random.randint(0, game.map_size[1] - 1)]
        # player_tank.game_object_type = EnumGameObjectType.Tank
        # game.game_objects.append(player_tank)

        # Iterate through the map grid
        for x in range(game.map_size[0]):
            for y in range(game.map_size[1]):
                # Randomly choose a game object type from the options
                game_object_type = random.choice(game_object_options)

                # If the game object type is Tank and the player's tank has not been set
                if game_object_type in [EnumGameObjectType.Enemy, EnumGameObjectType.EnemyAdvanced]:
                    game_object.tank_next_move_time = random.uniform(0, 2000)  # Start with a random time

                # If the game object type is not NotSet
                if game_object_type != EnumGameObjectType.NotSet:
                    # Clone the prototype GameObject instance
                    game_object = animated_game_object.clone()
                    game_object.position = [x, y]
                    game_object.game_object_type = game_object_type

                    # If the game object type is not NotSet
                    if game_object_type != EnumGameObjectType.NotSet:
                        # Clone the prototype GameObject instance
                        game_object = animated_game_object.clone()
                        game_object.position = [x, y]
                        game_object.game_object_type = game_object_type

                        # If the game object type is Steel, Brick, or Forest, disable animation
                        if game_object_type in [
                            EnumGameObjectType.Steel, EnumGameObjectType.Brick, EnumGameObjectType.Forest
                        ]:
                            game_object.animation_is_animating = False
                    # If the game object type is Steel, Brick, or Forest, disable animation
                    if game_object_type in [
                        EnumGameObjectType.Steel, EnumGameObjectType.Brick, EnumGameObjectType.Forest
                    ]:
                        game_object.animation_is_animating = False

                    # Add the game object to the game's list of game objects
                    game.game_objects.append(game_object)

    # def update(self, delta_time: float):
        # # Get the current game instance
        # game = self._game
        #
        # # Iterate through the game objects in the current game
        # for game_object in game.game_objects:
        #     # If the game object is of type Tank, EnemyAdvanced, or Enemy, update it using ControllerTank
        #     if game_object.game_object_type in [EnumGameObjectType.Tank, EnumGameObjectType.EnemyAdvanced,
        #                                         EnumGameObjectType.Enemy]:
        #         ControllerTank.update(game_object, game, delta_time)
        #     # If the game object is of type Bullet, update it using ControllerBullet
        #     elif game_object.game_object_type == EnumGameObjectType.Bullet:
        #         ControllerBullet.update(game_object, game, delta_time)
        #
        #     # If the game object is animating
        #     if game_object.animation_is_animating:
        #         # Increment the animation frame duration by the elapsed time (delta_time)
        #         game_object.animation_frame_duration += delta_time
        #
        #         # If the animation frame duration exceeds the maximum duration
        #         if game_object.animation_frame_duration >= game_object.animation_frame_duration_max:
        #             # Reset the animation frame duration
        #             game_object.animation_frame_duration = 0
        #
        #             # Increment the animation frame
        #             game_object.animation_frame += 1
        #
        #             # If the animation frame exceeds the maximum frame count, reset it to 0
        #             if game_object.animation_frame >= game_object.animation_frame_max:
        #                 game_object.animation_frame = 0

    def update(self, delta_time: float):
        """
        Update the state of the game and its objects based on the elapsed time.

        :param delta_time: The time elapsed since the last update, used to ensure smooth animations and movements.
        """
        # Retrieve the current game instance
        game = self._game

        # Iterate over each game object in the game's list of objects
        for game_object in game.game_objects:
            # Check if the game object is a Tank
            if game_object.game_object_type == EnumGameObjectType.Tank:
                # Update the tank using its controller logic
                ControllerTank.update(game_object, game, delta_time)

            # Check if the game object is an Enemy (either advanced or regular)
            elif game_object.game_object_type in [EnumGameObjectType.EnemyAdvanced, EnumGameObjectType.Enemy]:
                # Update the enemy using autonomous controller logic
                ControllerTank.update_autonomous(game_object, game, delta_time)

            # Check if the game object is a Bullet
            elif game_object.game_object_type == EnumGameObjectType.Bullet:
                # Update the bullet using its controller logic
                ControllerBullet.update(game_object, game, delta_time)

            # Handle animation updates for any animating game objects
            if game_object.animation_is_animating:
                # Increment the animation frame duration by the elapsed time
                game_object.animation_frame_duration += delta_time

                # Check if it's time to advance to the next animation frame
                if game_object.animation_frame_duration >= game_object.animation_frame_duration_max:
                    # Reset the frame duration counter
                    game_object.animation_frame_duration = 0

                    # Advance to the next frame in the animation sequence
                    game_object.animation_frame += 1

                    # Loop back to the first frame if we've reached the end of the animation sequence
                    if game_object.animation_frame >= game_object.animation_frame_max:
                        game_object.animation_frame = 0