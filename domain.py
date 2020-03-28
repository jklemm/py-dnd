from math import floor

import attr

from core.utils.dotted_dict import DottedDict


class Race(object):
    aditional_strength = 0
    aditional_constitution = 0
    aditional_dexterity = 0
    aditional_intelligence = 0
    aditional_wisdom = 0
    aditional_charisma = 0

    def __str__(self):
        return "Race"


class Dwarf(Race):
    aditional_strength = 2
    aditional_constitution = 2
    aditional_dexterity = 0
    aditional_intelligence = 0
    aditional_wisdom = 0
    aditional_charisma = 0

    def __str__(self):
        return "Dwarf"


class Halfling(Race):
    aditional_strength = 0
    aditional_constitution = 0
    aditional_dexterity = 2
    aditional_intelligence = 0
    aditional_wisdom = 0
    aditional_charisma = 0

    def __str__(self):
        return "Halfling"


# classes
default_klass = DottedDict(
    base_hp=0
)
barbarian = DottedDict(
    base_hp=12
)

XP_TO_LEVEL_LIST = [
    300, 900, 2700, 6500, 14000, 23000, 34000, 48000, 64000, 64000, 85000, 100000, 120000, 140000, 165000, 195000, 225000, 265000, 305000, 355000
]


@attr.s
class Character(object):
    # basic
    name = attr.ib(validator=attr.validators.instance_of(str))
    xp = attr.ib(validator=attr.validators.instance_of(int), default=0)
    hp = attr.ib(validator=attr.validators.instance_of(int), default=1)
    race = attr.ib(default=Race())
    klass = attr.ib(default=default_klass)

    # ability values
    base_strength = attr.ib(validator=attr.validators.instance_of(int), default=10)
    base_constitution = attr.ib(validator=attr.validators.instance_of(int), default=10)
    base_dexterity = attr.ib(validator=attr.validators.instance_of(int), default=10)
    base_intelligence = attr.ib(validator=attr.validators.instance_of(int), default=10)
    base_wisdom = attr.ib(validator=attr.validators.instance_of(int), default=10)
    base_charisma = attr.ib(validator=attr.validators.instance_of(int), default=10)

    @property
    def maximum_hp(self):
        return self.klass.base_hp + self.constitution_modifier

    @property
    def level(self):
        for index, xp_to_level in enumerate(XP_TO_LEVEL_LIST, start=1):
            if self.xp < xp_to_level:
                return index

    @property
    def strength(self):
        return self.base_strength + self.race.aditional_strength

    @property
    def constitution(self):
        return self.base_constitution + self.race.aditional_constitution

    @property
    def dexterity(self):
        return self.base_dexterity + self.race.aditional_dexterity

    @property
    def intelligence(self):
        return self.base_intelligence + self.race.aditional_intelligence

    @property
    def wisdom(self):
        return self.base_wisdom + self.race.aditional_wisdom

    @property
    def charisma(self):
        return self.base_charisma + self.race.aditional_charisma

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


def create_character():
    c = Character(name='Bruenor')
    c.race = Halfling()
    c.klass = barbarian
    c.hp = c.klass.base_hp + c.constitution_modifier
    return c


if __name__ == '__main__':
    c = create_character()

    print('name: ', c.name)
    print('race: ', c.race)
    print('klass: ', c.klass)
    print('level: ', c.level)
    print('xp: ', c.xp)
    print('hp: ', c.hp)
    print('maximum_hp: ', c.maximum_hp)
