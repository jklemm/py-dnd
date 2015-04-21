#!/usr/bin/python

import unittest

from core.structs.character_struct import CharacterStruct
from core.usecases.create_character_usecase import CreateCharacterUsecase
from core.gateways.character_gateway import CharacterGateway
from core.gateways.default_race_gateway import DefaultRaceGateway


class CreateCharacterUsecaseTests(unittest.TestCase):

    def setUp(self):
        self.character_gateway = CharacterGateway()

    def test_create_empty_character(self):
        character = CreateCharacterUsecase(self.character_gateway).execute()

        self.assertIsNotNone(character)
        self.assertIsInstance(character, CharacterStruct)
        self.assertEquals(character.strength, 0)
        self.assertEquals(character.constitution, 0)
        self.assertEquals(character.dexterity, 0)
        self.assertEquals(character.intelligence, 0)
        self.assertEquals(character.wisdom, 0)
        self.assertEquals(character.charisma, 0)

    def test_create_character_with_base_ability_score(self):
        self.character_gateway.set_base_ability_score(10, 10, 10, 10, 10, 10)
        character = CreateCharacterUsecase(self.character_gateway).execute()

        self.assertEquals(character.strength, 10)
        self.assertEquals(character.constitution, 10)
        self.assertEquals(character.dexterity, 10)
        self.assertEquals(character.intelligence, 10)
        self.assertEquals(character.wisdom, 10)
        self.assertEquals(character.charisma, 10)

    def test_create_default_race_character(self):
        race_gateway = DefaultRaceGateway()
        character = CreateCharacterUsecase(self.character_gateway, race_gateway).execute()

        self.assertEquals(character.strength, 0)
        self.assertEquals(character.constitution, 0)
        self.assertEquals(character.dexterity, 0)
        self.assertEquals(character.intelligence, 0)
        self.assertEquals(character.wisdom, 0)
        self.assertEquals(character.charisma, 0)

    def test_create_default_ability_score_race_character(self):
        race_gateway = DefaultRaceGateway()
        race_gateway.set_ability_score(10, 10, 10, 10, 10, 10)
        character = CreateCharacterUsecase(self.character_gateway, race_gateway).execute()

        self.assertEquals(character.strength, 10)
        self.assertEquals(character.constitution, 10)
        self.assertEquals(character.dexterity, 10)
        self.assertEquals(character.intelligence, 10)
        self.assertEquals(character.wisdom, 10)
        self.assertEquals(character.charisma, 10)

    def test_create_default_ability_score_race_character_with_base_ability_score(self):
        self.character_gateway.set_base_ability_score(10, 10, 10, 10, 10, 10)
        race_gateway = DefaultRaceGateway()
        race_gateway.set_ability_score(10, 10, 10, 10, 10, 10)
        character = CreateCharacterUsecase(self.character_gateway, race_gateway).execute()

        self.assertEquals(character.strength, 20)
        self.assertEquals(character.constitution, 20)
        self.assertEquals(character.dexterity, 20)
        self.assertEquals(character.intelligence, 20)
        self.assertEquals(character.wisdom, 20)
        self.assertEquals(character.charisma, 20)
