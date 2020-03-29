from math import floor, ceil

import attr


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


class Klass(object):
    health_dice = 0
    base_hp = 0

    def __str__(self):
        return "Klass"


class Barbarian(Klass):
    health_dice = 12
    base_hp = 12

    def __str__(self):
        return "Barbarian"


class Bard(Klass):
    health_dice = 8
    base_hp = 8

    def __str__(self):
        return "Bard"


XP_TO_LEVEL_LIST = [
    300, 900, 2700, 6500, 14000, 23000, 34000, 48000, 64000, 64000, 85000, 100000, 120000, 140000, 165000, 195000, 225000, 265000, 305000, 355000
]


@attr.s
class Character(object):
    # basic
    name = attr.ib(validator=attr.validators.instance_of(str))
    race = attr.ib(validator=attr.validators.instance_of((Dwarf, Halfling)))
    klass = attr.ib(validator=attr.validators.instance_of((Barbarian, Bard)))
    xp = attr.ib(validator=attr.validators.instance_of(int), default=0)
    hp = attr.ib(validator=attr.validators.instance_of(int), default=1)

    # ability values
    base_strength = attr.ib(validator=attr.validators.instance_of(int), default=10)
    base_constitution = attr.ib(validator=attr.validators.instance_of(int), default=10)
    base_dexterity = attr.ib(validator=attr.validators.instance_of(int), default=10)
    base_intelligence = attr.ib(validator=attr.validators.instance_of(int), default=10)
    base_wisdom = attr.ib(validator=attr.validators.instance_of(int), default=10)
    base_charisma = attr.ib(validator=attr.validators.instance_of(int), default=10)

    def __str__(self):
        msg = "Name: {}\n".format(c.name)
        msg += "Race: {}\n".format(c.race)
        msg += "Class: {}\n".format(c.klass)
        msg += "Level: {}\n".format(c.level)
        msg += "XP: {}\n".format(c.xp)
        msg += "HP: {} / {}\n".format(c.hp, c.maximum_hp)
        return msg

    @property
    def maximum_hp(self):
        return self.klass.base_hp + self.constitution_modifier

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
    c = Character(name='Bruenor', race=Halfling(), klass=Barbarian())
    c.hp = c.maximum_hp
    return c


if __name__ == '__main__':
    c = create_character()

    print(c)
