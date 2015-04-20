#!/usr/bin/python


class CharacterStruct(object):

    def __init__(self):
        self._strength = 0
        self._constitution = 0
        self._dexterity = 0
        self._intelligence = 0
        self._wisdom = 0
        self._charisma = 0
        self.race = None

    @property
    def strength(self):
        return self._strength + self.race.strength

    @property
    def constitution(self):
        return self._constitution + self.race.constitution

    @property
    def dexterity(self):
        return self._dexterity + self.race.dexterity

    @property
    def intelligence(self):
        return self._intelligence + self.race.intelligence

    @property
    def wisdom(self):
        return self._wisdom + self.race.wisdom

    @property
    def charisma(self):
        return self._charisma + self.race.charisma
