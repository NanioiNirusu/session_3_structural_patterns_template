import random
from typing import Tuple, List

import pygame
from pygame import Surface

from models.GameObject import GameObject
from models.enums.EnumGameObjectType import EnumGameObjectType
from views.components.base.ComponentBase import ComponentBase

import os

current_dir = os.path.dirname(__file__)

# Load the sprite sheet containing the Battle City game objects
battle_city_sprites = pygame.image.load(os.path.join(current_dir, '..', '..', 'resources', 'images', 'battle_city_sprites.png'))

# Define the width of each sprite in the sprite sheet
sprite_width = 32

# Define the size of each sprite as a tuple (width, height)
sprite_size = (sprite_width, sprite_width)


class ComponentGameObject(ComponentBase):
    def __init__(
            self,
            game_object: GameObject,
    ):
        super().__init__()

        # Store the GameObject instance associated with this component
        self.game_object = game_object

        # Initialize an empty list to store the pygame surfaces for this game object
        self.pygame_surfaces: List[pygame.Surface] = []

        # Load the appropriate surface based on the game object type
        if self.game_object.game_object_type == EnumGameObjectType.Brick:
            self.load_surface(sprite_x=16, sprite_y=0)
        elif self.game_object.game_object_type == EnumGameObjectType.Steel:
            self.load_surface(sprite_x=16, sprite_y=1)
        elif self.game_object.game_object_type == EnumGameObjectType.Forest:
            self.load_surface(sprite_x=17, sprite_y=2)
        elif self.game_object.game_object_type == EnumGameObjectType.Water:
            self.load_surface(sprite_x=16, sprite_y=2)
            self.load_surface(sprite_x=16, sprite_y=3)

    def load_surface(self, sprite_x, sprite_y):
        # Create a new surface with the specified sprite size
        surface = pygame.Surface(size=sprite_size)

        # Blit the specific sprite from the sprite sheet onto the surface
        surface.blit(
            battle_city_sprites,
            dest=(0, 0),
            area=(
                sprite_x * sprite_width,
                sprite_y * sprite_width,
                sprite_width,
                sprite_width
            )
        )

        # Append the loaded surface to the list of surfaces for this game object
        self.pygame_surfaces.append(surface)

        # Return the loaded surface
        return surface

    def update(self, delta_milisec):
        # This method is called every frame to update the game object
        # In this case, it does nothing and can be overridden in derived classes
        pass

    def render(self, screen: Surface):
        # Check if the current animation frame is within the range of available surfaces
        if self.game_object.animation_frame < len(self.pygame_surfaces):
            # Blit the surface corresponding to the current animation frame onto the screen
            screen.blit(
                self.pygame_surfaces[self.game_object.animation_frame],
                (self.game_object.position[0] * sprite_width, self.game_object.position[1] * sprite_width)
            )

    def on_mouse_move(self, mouse_position: Tuple[int, int]):
        # This method is called when the mouse is moved
        # In this case, it does nothing and can be overridden in derived classes
        pass

    def on_mouse_button_down(self):
        # This method is called when a mouse button is pressed down
        # In this case, it does nothing and can be overridden in derived classes
        pass

    def on_mouse_button_up(self):
        # This method is called when a mouse button is released
        # In this case, it does nothing and can be overridden in derived classes
        pass