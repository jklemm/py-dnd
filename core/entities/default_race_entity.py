from core.structs import AbilityScoreStruct
from core.structs import RaceStruct


class DefaultRaceEntity(object):
    def __init__(self):
        self.race = RaceStruct()

    def get_struct(self):
        return self.race

    def set_ability_score(self, strength=0, constitution=0, dexterity=0, intelligence=0, wisdom=0, charisma=0):
        ability_score = AbilityScoreStruct(strength, constitution, dexterity, intelligence, wisdom, charisma)
        self.race.ability_score = ability_score
