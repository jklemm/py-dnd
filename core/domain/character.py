from math import floor, ceil

from pydantic.v1 import BaseModel, PositiveInt

from core.domain.klasses import BaseKlass
from core.domain.races import BaseRace

XP_TO_LEVEL_LIST = [
    300, 900, 2700, 6500, 14000, 23000, 34000, 48000, 64000, 64000, 85000, 100000, 120000, 140000, 165000, 195000, 225000, 265000, 305000, 355000
]


class Character(BaseModel):
    # basic
    name: str = ''
    race: BaseRace = None
    klass: BaseKlass = None
    xp: PositiveInt = 0
    hp: PositiveInt = 1

    # ability values
    base_strength: PositiveInt = 10
    base_constitution: PositiveInt = 10
    base_dexterity: PositiveInt = 10
    base_intelligence: PositiveInt = 10
    base_wisdom: PositiveInt = 10
    base_charisma: PositiveInt = 10

    base_armor_class: PositiveInt = 10

    def __str__(self):
        return '' \
            f'Name: {self.name}\n' \
            f'Race: {self.race}\n' \
            f'Class: {self.klass}\n' \
            f'Level: {self.level}\n' \
            f'XP: {self.xp}\n' \
            f'HP: {self.hp} / {self.maximum_hp}'

    @property
    def maximum_hp(self):
        return self.klass.base_hp + self.constitution_modifier

    @property
    def armor_class(self):
        return self.base_armor_class + self.dexterity_modifier

    @property
    def level(self):
        for index, xp_to_level in enumerate(XP_TO_LEVEL_LIST, start=1):
            if self.xp < xp_to_level:
                return index

    @property
    def proficiency_bonus(self):
        return ceil(self.level / 4) + 1

    @property
    def strength(self):
        return self.base_strength + self.race.additional_strength

    @property
    def constitution(self):
        return self.base_constitution + self.race.additional_constitution

    @property
    def dexterity(self):
        return self.base_dexterity + self.race.additional_dexterity

    @property
    def intelligence(self):
        return self.base_intelligence + self.race.additional_intelligence

    @property
    def wisdom(self):
        return self.base_wisdom + self.race.additional_wisdom

    @property
    def charisma(self):
        return self.base_charisma + self.race.additional_charisma

    @property
    def strength_modifier(self):
        return floor(self.base_strength - 10)

    @property
    def constitution_modifier(self):
        return floor(self.base_constitution - 10)

    @property
    def dexterity_modifier(self):
        return floor(self.base_dexterity - 10)

    @property
    def intelligence_modifier(self):
        return floor(self.base_intelligence - 10)

    @property
    def wisdom_modifier(self):
        return floor(self.base_wisdom - 10)

    @property
    def charisma_modifier(self):
        return floor(self.base_charisma - 10)
