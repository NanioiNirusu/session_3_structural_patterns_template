from typing import List

from models.enums.EnumGameObjectType import EnumGameObjectType
from models.GameObject import GameObject
from views.components.ComponentBullet import ComponentBullet
from views.components.ComponentEnemy import ComponentEnemy
from views.components.ComponentGameObject import ComponentGameObject
from views.components.ComponentTank import ComponentTank


class FactoryGameObject:
    def create_component(self, game_objet:GameObject) ->ComponentGameObject:
        obj_type = game_objet.game_object_type
        if obj_type == EnumGameObjectType.Tank:
            result = ComponentTank(game_objet)
        elif obj_type == EnumGameObjectType.Bullet:
            result = ComponentBullet(game_objet)
        elif obj_type in [EnumGameObjectType.Enemy, EnumGameObjectType.EnemyAdvanced]:
            result = ComponentEnemy(game_objet)
        else:
            result = ComponentGameObject(game_objet)
        return result
