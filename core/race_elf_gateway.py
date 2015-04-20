#!/usr/bin/python


class AbilityScoreStruct(object):

    def __init__(self):
        self.strength = 0
        self.constitution = 0
        self.dexterity = 0
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 0


class ElfRaceGateway(object):

    def __init__(self):
        self.bonus_ability_score = AbilityScoreStruct()
        self.bonus_ability_score.dexterity = 2
        self.bonus_ability_score.wisdom = 2

    def get_bonus_ability_score_struct(self):
        return self.bonus_ability_score
