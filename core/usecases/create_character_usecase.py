#!/usr/bin/python
from core.entities.default_race_entity import DefaultRaceEntity


class CreateCharacterUsecase():

    def __init__(self, character_gateway, race_entity=None):
        self.character_gateway = character_gateway
        self.race_entity = race_entity or DefaultRaceEntity()

    def execute(self):
        self.character_gateway.race_entity = self.race_entity
        return self.character_gateway.create_character()
