from typing import List

import pygame
from pygame import Surface

from models.GameObject import GameObject
from models.enums.EnumGameObjectDirection import EnumGameObjectDirection
from views.components.ComponentGameObject import ComponentGameObject


class ComponentTank(ComponentGameObject):
    def __init__(self, game_object: GameObject):
        # Call the constructor of the parent class (ComponentGameObject)
        super().__init__(game_object)

        # Initialize lists to store the pygame surfaces for different directions
        self.pygame_surfaces_up: List[pygame.Surface] = []
        self.pygame_surfaces_down: List[pygame.Surface] = []
        self.pygame_surfaces_left: List[pygame.Surface] = []
        self.pygame_surfaces_right: List[pygame.Surface] = []

        # Load and append the pygame surfaces for the "up" direction
        self.pygame_surfaces_up.append(self.load_surface(sprite_x=0, sprite_y=0))
        self.pygame_surfaces_up.append(self.load_surface(sprite_x=1, sprite_y=0))

        # Load and append the pygame surfaces for the "left" direction
        self.pygame_surfaces_left.append(self.load_surface(sprite_x=2, sprite_y=0))
        self.pygame_surfaces_left.append(self.load_surface(sprite_x=3, sprite_y=0))

        # Load and append the pygame surfaces for the "down" direction
        self.pygame_surfaces_down.append(self.load_surface(sprite_x=4, sprite_y=0))
        self.pygame_surfaces_down.append(self.load_surface(sprite_x=5, sprite_y=0))

        # Load and append the pygame surfaces for the "right" direction
        self.pygame_surfaces_right.append(self.load_surface(sprite_x=6, sprite_y=0))
        self.pygame_surfaces_right.append(self.load_surface(sprite_x=7, sprite_y=0))

        # Set the initial pygame surfaces to the "up" direction
        self.pygame_surfaces = self.pygame_surfaces_up


    def update(self, delta_milisec):
        # Check the direction of the game object and set the corresponding pygame surfaces
        if self.game_object.direction == EnumGameObjectDirection.Up:
            self.pygame_surfaces = self.pygame_surfaces_up
        elif self.game_object.direction == EnumGameObjectDirection.Down:
            self.pygame_surfaces = self.pygame_surfaces_down
        elif self.game_object.direction == EnumGameObjectDirection.Left:
            self.pygame_surfaces = self.pygame_surfaces_left
        elif self.game_object.direction == EnumGameObjectDirection.Right:
            self.pygame_surfaces = self.pygame_surfaces_right

        # Call the update method of the parent class (ComponentGameObject)
        super().update(delta_milisec)


    def render(self, screen: Surface):
        # Call the render method of the parent class (ComponentGameObject)
        super().render(screen)
