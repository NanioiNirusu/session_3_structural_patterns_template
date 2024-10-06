from controllers.ControllerGame import ControllerGame
from controllers.ControllerTank import ControllerTank
from models.GameObject import GameObject


# The ControllerPlayer class implements the singleton pattern.
# It ensures only one instance of the class can be created.
# This class will store a pointer to the player GameObject.
class ControllerPlayer:

    # Class variable to store the single instance
    _instance = None

    # Private constructor that takes the player GameObject as a parameter
    def __init__(self, player: GameObject):
        # Check if an instance already exists
        if ControllerPlayer._instance is not None:
            # If an instance exists, raise an exception to prevent creating another one
            raise Exception("Cannot initialize singleton twice")
        # Set the instance to the current object
        ControllerPlayer._instance = self
        # Store the player GameObject
        self._player = player

    # Static method to get the single instance of the class
    @staticmethod
    def instance():
        # Check if no instance has been created yet
        if ControllerPlayer._instance is None:
            # If no instance exists, create one with None as the player GameObject
            ControllerPlayer._instance = ControllerPlayer(None)
        # Return the single instance
        return ControllerPlayer._instance

    # Method to make the player fire
    def fire(self):
        # Call the fire method of ControllerTank, passing the player GameObject and the current game instance
        ControllerTank.fire(self._player, ControllerGame.instance().game)

    # Method to set the direction of the player
    def set_direction(self, direction):
        # Call the set_direction method of ControllerTank, passing the player GameObject and the desired direction
        ControllerTank.set_direction(self._player, direction)