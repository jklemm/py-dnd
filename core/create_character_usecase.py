
class CreateCharacterUsecase():

    def __init__(self, character_gateway, race_gateway):
        self.character_gateway = character_gateway
        self.race_gateway = race_gateway

    def execute(self):
        race_struct = self.race_gateway.get_bonus_ability_score_struct() if self.race_gateway else None
        return self.character_gateway.create_character(race_struct)
