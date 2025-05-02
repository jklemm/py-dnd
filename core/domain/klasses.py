from pydantic.v1 import BaseModel, PositiveInt


class BaseKlass(BaseModel):
    health_dice: PositiveInt = 0
    base_hp: PositiveInt = 0


class Barbarian(BaseKlass):
    health_dice: PositiveInt = 12
    base_hp: PositiveInt = 12

    def __str__(self):
        return 'Barbarian'


class Bard(BaseKlass):
    health_dice: PositiveInt = 8
    base_hp: PositiveInt = 8

    def __str__(self):
        return 'Bard'
