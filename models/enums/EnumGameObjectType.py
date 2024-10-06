from enum import Enum


class EnumGameObjectType(str, Enum):
    NotSet = "NotSet"
    Forest = "Forest"
    Water = "Water"
    Brick = "Brick"
    Steel = "Steel"
    Tank = "Tank"
    Enemy = "Enemy"
    EnemyAdvanced = "EnemyAdvanced"
    Bullet = "Bullet"
