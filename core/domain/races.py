from enum import unique, IntEnum


@unique
class RaceEnum(IntEnum):
    DWARF = 1
    HALFLING = 2


def get_race(race: RaceEnum):
    races = {
        RaceEnum.DWARF: Dwarf,
        RaceEnum.HALFLING: Halfling,
    }
    selected_race = races.get(race)
    return selected_race()


class Dwarf:
    aditional_strength = 2
    aditional_constitution = 2
    aditional_dexterity = 0
    aditional_intelligence = 0
    aditional_wisdom = 0
    aditional_charisma = 0

    def __str__(self):
        return "Dwarf"


class Halfling:
    aditional_strength = 0
    aditional_constitution = 0
    aditional_dexterity = 2
    aditional_intelligence = 0
    aditional_wisdom = 0
    aditional_charisma = 0

    def __str__(self):
        return "Halfling"
