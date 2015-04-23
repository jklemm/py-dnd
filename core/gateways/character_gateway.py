from core.structs import AbilityScoreStruct
from core.structs import CharacterStruct


class CharacterGateway(object):
    def __init__(self):
        self.ability_score = AbilityScoreStruct()
        self.character_struct = None
        self.race_gateway = None

    def create_character(self):
        self.character_struct = CharacterStruct()
        self.character_struct.ability_score = self.ability_score
        self.character_struct.race = self.race_gateway.get_struct() if self.race_gateway else None
        return self.character_struct

    def set_ability_score(self, strength=0, constitution=0, dexterity=0, intelligence=0, wisdom=0, charisma=0):
        self.ability_score = AbilityScoreStruct(strength, constitution, dexterity, intelligence, wisdom, charisma)
