from pydantic.v1 import BaseModel, PositiveInt


class BaseRace(BaseModel):
    additional_strength: PositiveInt = 0
    additional_constitution: PositiveInt = 0
    additional_dexterity: PositiveInt = 0
    additional_intelligence: PositiveInt = 0
    additional_wisdom: PositiveInt = 0
    additional_charisma: PositiveInt = 0


class Dwarf(BaseRace):
    additional_strength: PositiveInt = 2
    additional_constitution: PositiveInt = 2

    def __str__(self):
        return 'Dwarf'


class Halfling(BaseRace):
    additional_dexterity: PositiveInt = 2

    def __str__(self):
        return 'Halfling'
