from controllers.ControllerGame import ControllerGame
from controllers.ControllerTank import ControllerTank
from models.GameObject import GameObject


# singleton pattern of ControllerTank, will store pointer to GameObject player
class ControllerPlayer:

    _instance = None

    def __init__(self, player: GameObject):
        if ControllerPlayer._instance is not None:
            raise Exception("Cannot initialize singleton twice")
        ControllerPlayer._instance = self
        self._player = player

    @staticmethod
    def instance():
        if ControllerPlayer._instance is None:
            ControllerPlayer._instance = ControllerPlayer(None)
        return ControllerPlayer._instance

    def fire(self):
        ControllerTank.fire(self._player, ControllerGame.instance().game)

    def set_direction(self, direction):
        ControllerTank.set_direction(self._player, direction)
