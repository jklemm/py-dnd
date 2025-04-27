class CharacterStruct:
    def __init__(self):
        from core.structs.ability_score_struct import AbilityScoreStruct
        from core.structs.race_struct import RaceStruct
        self.ability_score = AbilityScoreStruct()
        self.race = RaceStruct()

    @property
    def strength(self):
        return self.ability_score.strength + self.race.ability_score.strength

    @property
    def constitution(self):
        return self.ability_score.constitution + self.race.ability_score.constitution

    @property
    def dexterity(self):
        return self.ability_score.dexterity + self.race.ability_score.dexterity

    @property
    def intelligence(self):
        return self.ability_score.intelligence + self.race.ability_score.intelligence

    @property
    def wisdom(self):
        return self.ability_score.wisdom + self.race.ability_score.wisdom

    @property
    def charisma(self):
        return self.ability_score.charisma + self.race.ability_score.charisma
