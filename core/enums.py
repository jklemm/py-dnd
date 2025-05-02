from enum import unique, IntEnum, auto


@unique
class RaceEnum(IntEnum):
    DWARF = auto()
    HALFLING = auto()


@unique
class KlassEnum(IntEnum):
    BARBARIAN = auto()
    BARD = auto()
