#!/usr/bin/python

import unittest
from core.character_struct import CharacterStruct
from core.create_character_usecase import CreateCharacterUsecase
from core.character_gateway import CharacterGateway
from core.race_elf_gateway import ElfRaceGateway


class CreateCharacterUsecaseTests(unittest.TestCase):

    def setUp(self):
        self.character_gateway = CharacterGateway()

    def test_create_empty_character(self):
        race_gateway = RaceGatewayFake()
        character = CreateCharacterUsecase(self.character_gateway, race_gateway).execute()

        self.assertIsNotNone(character)
        self.assertIsInstance(character, CharacterStruct)

    def test_create_character_with_ability_scores(self):
        race_gateway = RaceGatewayFake()
        character = CreateCharacterUsecase(self.character_gateway, race_gateway).execute()

        self.assertTrue(hasattr(character, 'strength'))
        self.assertTrue(hasattr(character, 'constitution'))
        self.assertTrue(hasattr(character, 'dexterity'))
        self.assertTrue(hasattr(character, 'intelligence'))
        self.assertTrue(hasattr(character, 'wisdom'))
        self.assertTrue(hasattr(character, 'charisma'))

    def test_create_character_with_no_race(self):
        race_gateway = None
        character = CreateCharacterUsecase(self.character_gateway, race_gateway).execute()

        self.assertEquals(character.strength, 0)
        self.assertEquals(character.constitution, 0)
        self.assertEquals(character.dexterity, 0)
        self.assertEquals(character.intelligence, 0)
        self.assertEquals(character.wisdom, 0)
        self.assertEquals(character.charisma, 0)

    def test_create_elf_race_character(self):
        race_gateway = ElfRaceGateway()
        character = CreateCharacterUsecase(self.character_gateway, race_gateway).execute()

        self.assertEquals(character.strength, 0)
        self.assertEquals(character.constitution, 0)
        self.assertEquals(character.dexterity, 2)
        self.assertEquals(character.intelligence, 0)
        self.assertEquals(character.wisdom, 2)
        self.assertEquals(character.charisma, 0)


class RaceGatewayFake(object):

    def get_bonus_ability_score_struct(self):
        return None
