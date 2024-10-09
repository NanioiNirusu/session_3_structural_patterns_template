from abc import ABC, abstractmethod
from models.Game import Game


# Abstract base class for building game levels
class LevelBuilder(ABC):
    @abstractmethod
    def build_level(self, game: Game):
        """
        Abstract method to be implemented by subclasses.
        This method will define how a level is built for the given game.

        :param game: An instance of the Game class where the level will be built.
        """
        pass


# Concrete class for building level 1 of the game
class Level1Builder(LevelBuilder):
    def build_level(self, game: Game):
        """
        Implementation of the build_level method for level 1.
        This method contains the logic specific to constructing level 1 in the game.

        :param game: An instance of the Game class where level 1 will be built.
        """
        # Implementation for building level 1
        pass


# Concrete class for building level 2 of the game
class Level2Builder(LevelBuilder):
    def build_level(self, game: Game):
        """
        Implementation of the build_level method for level 2.
        This method contains the logic specific to constructing level 2 in the game.

        :param game: An instance of the Game class where level 2 will be built.
        """
        # Implementation for building level 2
        pass