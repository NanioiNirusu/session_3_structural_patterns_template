from typing import List

from models.enums.EnumGameObjectType import EnumGameObjectType
from models.GameObject import GameObject
from views.components.ComponentBullet import ComponentBullet
from views.components.ComponentEnemy import ComponentEnemy
from views.components.ComponentGameObject import ComponentGameObject
from views.components.ComponentTank import ComponentTank


class FactoryGameObject:
    def create_component(self, game_objet: GameObject) -> ComponentGameObject:
        # Get the game object type from the game_objet parameter
        obj_type = game_objet.game_object_type

        # Check the game object type and create the corresponding component
        if obj_type == EnumGameObjectType.Tank:
            # If the game object type is Tank, create a ComponentTank instance
            result = ComponentTank(game_objet)
        elif obj_type == EnumGameObjectType.Bullet:
            # If the game object type is Bullet, create a ComponentBullet instance
            result = ComponentBullet(game_objet)
        elif obj_type in [EnumGameObjectType.Enemy, EnumGameObjectType.EnemyAdvanced]:
            # If the game object type is Enemy or EnemyAdvanced, create a ComponentEnemy instance
            result = ComponentEnemy(game_objet)
        else:
            # For any other game object type, create a generic ComponentGameObject instance
            result = ComponentGameObject(game_objet)

        # Return the created component
        return result