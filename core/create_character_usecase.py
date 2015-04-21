#!/usr/bin/python
from core.default_race_gateway import DefaultRaceGateway


class CreateCharacterUsecase():

    def __init__(self, character_gateway, race_gateway=None):
        self.character_gateway = character_gateway
        self.race_gateway = race_gateway or DefaultRaceGateway()

    def execute(self):
        self.character_gateway.race_gateway = self.race_gateway
        return self.character_gateway.create_character()
