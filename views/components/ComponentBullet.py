from typing import List

import pygame
from pygame import Surface

from models.GameObject import GameObject
from models.enums.EnumGameObjectDirection import EnumGameObjectDirection
from views.components.ComponentGameObject import ComponentGameObject


class ComponentBullet(ComponentGameObject):
    def __init__(self, game_object: GameObject):
        # Call the parent class constructor
        super().__init__(game_object)

        # Initialize lists to store pygame surfaces for different directions
        self.pygame_surfaces_up: List[pygame.Surface] = []
        self.pygame_surfaces_down: List[pygame.Surface] = []
        self.pygame_surfaces_left: List[pygame.Surface] = []
        self.pygame_surfaces_right: List[pygame.Surface] = []

        # Load the surface for the bullet facing up
        self.pygame_surfaces_up.append(self.load_surface(sprite_x=19, sprite_y=5))

        # Load the surface for the bullet facing left
        self.pygame_surfaces_left.append(self.load_surface(sprite_x=20, sprite_y=5))

        # Load the surface for the bullet facing down
        self.pygame_surfaces_down.append(self.load_surface(sprite_x=21, sprite_y=5))

        # Load the surface for the bullet facing right
        self.pygame_surfaces_right.append(self.load_surface(sprite_x=22, sprite_y=5))

        # Set the initial pygame surfaces to the surfaces for the bullet facing up
        self.pygame_surfaces = self.pygame_surfaces_up


    def update(self, delta_milisec):
        # Check the direction of the game object
        if self.game_object.direction == EnumGameObjectDirection.Up:
            # Set the pygame surfaces to the surfaces for the bullet facing up
            self.pygame_surfaces = self.pygame_surfaces_up
        elif self.game_object.direction == EnumGameObjectDirection.Down:
            # Set the pygame surfaces to the surfaces for the bullet facing down
            self.pygame_surfaces = self.pygame_surfaces_down
        elif self.game_object.direction == EnumGameObjectDirection.Left:
            # Set the pygame surfaces to the surfaces for the bullet facing left
            self.pygame_surfaces = self.pygame_surfaces_left
        elif self.game_object.direction == EnumGameObjectDirection.Right:
            # Set the pygame surfaces to the surfaces for the bullet facing right
            self.pygame_surfaces = self.pygame_surfaces_right

        # Call the parent class update method
        super().update(delta_milisec)


    def render(self, screen: Surface):
        # Call the parent class render method
        super().render(screen)