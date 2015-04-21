#!/usr/bin/python
from core.ability_score_struct import AbilityScoreStruct
from core.race_struct import RaceStruct


class CharacterStruct(object):

    def __init__(self):
        self.ability_score = AbilityScoreStruct()
        self.race = RaceStruct()

    @property
    def strength(self):
        base_strength = self.ability_score.strength
        race_strength = self.race.ability_score.strength
        return base_strength + race_strength

    @property
    def constitution(self):
        base_constitution = self.ability_score.constitution
        race_constitution = self.race.ability_score.constitution
        return base_constitution + race_constitution

    @property
    def dexterity(self):
        base_dexterity = self.ability_score.dexterity
        race_dexterity = self.race.ability_score.dexterity
        return base_dexterity + race_dexterity

    @property
    def intelligence(self):
        base_intelligence = self.ability_score.intelligence
        race_intelligence = self.race.ability_score.intelligence
        return base_intelligence + race_intelligence

    @property
    def wisdom(self):
        base_wisdom = self.ability_score.wisdom
        race_wisdom = self.race.ability_score.wisdom
        return base_wisdom + race_wisdom

    @property
    def charisma(self):
        base_charisma = self.ability_score.charisma
        race_charisma = self.race.ability_score.charisma
        return base_charisma + race_charisma
