from enum import unique, IntEnum


@unique
class KlassEnum(IntEnum):
    BARBARIAN = 1
    BARD = 2


def get_klass(klass: KlassEnum):
    klasses = {
        KlassEnum.BARBARIAN: Barbarian,
        KlassEnum.BARD: Bard,
    }
    selected_klass = klasses.get(klass)
    return selected_klass()


class Barbarian:
    health_dice = 12
    base_hp = 12

    def __str__(self):
        return "Barbarian"


class Bard:
    health_dice = 8
    base_hp = 8

    def __str__(self):
        return "Bard"
