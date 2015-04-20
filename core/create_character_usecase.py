
class CreateCharacterUsecase():

    def __init__(self, character_gateway):
        self.character_gateway = character_gateway

    def execute(self):
        return self.character_gateway.create_character()
