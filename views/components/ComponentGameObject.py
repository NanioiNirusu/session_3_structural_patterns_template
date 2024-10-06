import random
from typing import Tuple, List

import pygame
from pygame import Surface

from models.GameObject import GameObject
from models.enums.EnumGameObjectType import EnumGameObjectType
from views.components.base.ComponentBase import ComponentBase

battle_city_sprites = pygame.image.load('./resources/images/battle_city_sprites.png')
sprite_width = 32
sprite_size = (sprite_width, sprite_width)


class ComponentGameObject(ComponentBase):
    def __init__(
            self,
            game_object: GameObject,
    ):
        super().__init__()

        self.game_object = game_object

        self.pygame_surfaces: List[pygame.Surface] = []

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
        surface = pygame.Surface(size=sprite_size)
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
        self.pygame_surfaces.append(surface)
        return surface

    def update(self, delta_milisec):
        pass

    def render(self, screen: Surface):
        if self.game_object.animation_frame < len(self.pygame_surfaces):
            screen.blit(
                self.pygame_surfaces[self.game_object.animation_frame],
                (self.game_object.position[0] * sprite_width, self.game_object.position[1] * sprite_width)
            )

    def on_mouse_move(self, mouse_position: Tuple[int, int]):
        pass

    def on_mouse_button_down(self):
        pass

    def on_mouse_button_up(self):
        pass


