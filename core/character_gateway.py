#!/usr/bin/python
from core.ability_score_struct import AbilityScoreStruct
from core.character_struct import CharacterStruct


class CharacterGateway(object):

    def __init__(self):
        self.base_ability_score = AbilityScoreStruct()
        self.character_struct = None
        self.race_gateway = None

    def create_character(self):
        self.character_struct = CharacterStruct()
        self.character_struct.ability_score = self.base_ability_score
        self.character_struct.race = self.race_gateway.get_struct() if self.race_gateway else None
        return self.character_struct

    def set_base_ability_score(self, strength=0, constitution=0, dexterity=0, intelligence=0, wisdom=0, charisma=0):
        self.base_ability_score = AbilityScoreStruct(strength, constitution, dexterity, intelligence, wisdom, charisma)
