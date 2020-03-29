class Dwarf(object):
    aditional_strength = 2
    aditional_constitution = 2
    aditional_dexterity = 0
    aditional_intelligence = 0
    aditional_wisdom = 0
    aditional_charisma = 0

    def __str__(self):
        return "Dwarf"


class Halfling(object):
    aditional_strength = 0
    aditional_constitution = 0
    aditional_dexterity = 2
    aditional_intelligence = 0
    aditional_wisdom = 0
    aditional_charisma = 0

    def __str__(self):
        return "Halfling"
