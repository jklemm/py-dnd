#!/usr/bin/python


class CharacterGateway(object):

    def create_character(self, race_bonus_ability_score_struct):
        from core.character_struct import CharacterStruct
        character_struct = CharacterStruct()
        character_struct.race = race_bonus_ability_score_struct
        return character_struct
