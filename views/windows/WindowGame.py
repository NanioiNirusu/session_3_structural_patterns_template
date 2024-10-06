import time
from typing import List

import pygame
from pygame import Surface

from controllers.ControllerGame import ControllerGame
from controllers.ControllerPlayer import ControllerPlayer
from controllers.ControllerTank import ControllerTank
from models.enums.EnumGameObjectDirection import EnumGameObjectDirection
from models.enums.EnumGameObjectType import EnumGameObjectType
from views.components.ComponentEnemy import ComponentEnemy
from views.components.ComponentGameObject import ComponentGameObject, sprite_width
from views.components.ComponentTank import ComponentTank
from views.components.base import ComponentBase
from views.factories.FactoryGameObject import FactoryGameObject
from views.components.ComponentBullet import ComponentBullet

class WindowGame:
    def __init__(self):
        super().__init__()

        ControllerGame.instance().new_game()
        game = ControllerGame.instance().game
        self.screen = pygame.display.set_mode(
            (game.map_size[0] * sprite_width, game.map_size[1] * sprite_width)
        )
        self.is_game_running = True
        self.set_game()
        self.factory_game_object = FactoryGameObject()

        self.unused_components_by_type = {
            EnumGameObjectType.Tank: [],
            EnumGameObjectType.Enemy: [],
            EnumGameObjectType.Bullet: [],
            EnumGameObjectType.Brick: [],
            EnumGameObjectType.Steel: [],
            EnumGameObjectType.Water: [],
            EnumGameObjectType.Forest: [],
        }



    def set_game(self):
        self.game_components: List[ComponentBase] = []
        ControllerPlayer(ControllerGame.instance().player())

    def show(self):
        self.is_game_running = True
        # main game loop
        time_last = pygame.time.get_ticks()
        while self.is_game_running:
            # get delta seconds
            time_current = pygame.time.get_ticks()
            delta_milisec = time_current - time_last
            time_last = time_current

            # update
            self.update(delta_milisec)

            # draw
            self.render()

            # update display
            pygame.display.flip()
            time.sleep(0.01)

    def sync_game_components(self):
        # TODO pool pattern
        # remove missing game_components
        existing_game_objects = []
        for game_component in self.game_components:
            if game_component.game_object not in ControllerGame.instance().game.game_objects:
                self.game_components.remove(game_component)

                self.unused_components_by_type[game_component.game_object.game_object_type].append(game_component)
            else:
                existing_game_objects.append(game_component.game_object)

        # add new game_components
        for game_object in ControllerGame.instance().game.game_objects:
            if game_object not in existing_game_objects:
                if len(self.unused_components_by_type[game_object.game_object_type]) > 0:
                # TODO factory pattern
                    component = self.unused_components_by_type[game_object.game_object_type].pop()
                    component.game_object = game_object
                else:
                    component = self.factory_game_object.create_component(game_object)
                self.game_components.append(component)


    def update(self, delta_milisec):
        ControllerGame.instance().update(delta_milisec)

        self.sync_game_components()

        for game_component in self.game_components:
            game_component.update(delta_milisec)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.is_game_running = False
                elif event.key == pygame.K_UP:
                    ControllerPlayer.instance().set_direction(EnumGameObjectDirection.Up)
                    # ControllerTank.set_direction(ControllerGame.instance().player(), EnumGameObjectDirection.Up)
                elif event.key == pygame.K_DOWN:
                    ControllerPlayer.instance().set_direction(EnumGameObjectDirection.Down)
                    # ControllerTank.set_direction(ControllerGame.instance().player(), EnumGameObjectDirection.Down)
                elif event.key == pygame.K_LEFT:
                    ControllerPlayer.instance().set_direction(EnumGameObjectDirection.Left)
                    # ControllerTank.set_direction(ControllerGame.instance().player(), EnumGameObjectDirection.Left)
                elif event.key == pygame.K_RIGHT:
                    ControllerPlayer.instance().set_direction(EnumGameObjectDirection.Right)
                    # ControllerTank.set_direction(ControllerGame.instance().player(), EnumGameObjectDirection.Right)
            elif event.type == pygame.KEYUP:
                if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                    ControllerTank.set_direction(ControllerGame.instance().player(), EnumGameObjectDirection.NotSet)
                if event.key == pygame.K_SPACE:
                    ControllerTank.fire(ControllerGame.instance().player(), ControllerGame.instance().game)

    def render(self):
        self.screen.fill((0, 0, 0))
        for game_component in self.game_components:
            game_component.render(self.screen)

        font = pygame.font.SysFont('arial', 20)
        img_font = font.render(f"score: {ControllerGame.instance().game.score}", True, (255, 255, 255))
        self.screen.blit(img_font, (0, 0))