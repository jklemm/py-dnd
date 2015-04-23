from unittest import TestCase
from core.gateways.dwarf_race_gateway import DwarfRaceGateway
from core.gateways.elf_race_gateway import ElfRaceGateway
from core.structs.character_struct import CharacterStruct
from core.usecases.create_character_usecase import CreateCharacterUsecase
from core.gateways.character_gateway import CharacterGateway
from core.gateways.default_race_gateway import DefaultRaceGateway


class CreateCharacterUsecaseTests(TestCase):
    def test_not_none(self):
        character_gateway = CharacterGateway()
        character = CreateCharacterUsecase(character_gateway).execute()

        self.assertIsNotNone(character)
        self.assertIsInstance(character, CharacterStruct)


class CharacterGatewayTests(TestCase):
    def setUp(self):
        self.character_gateway = CharacterGateway()
        self.race_gateway = DefaultRaceGateway()

    def test_not_none(self):
        character = self.character_gateway.create_character()
        self.assertIsNotNone(character)
        self.assertIsInstance(character, CharacterStruct)

    def test_create_an_empty_character(self):
        self.character_gateway.race_gateway = self.race_gateway
        character = self.character_gateway.create_character()

        self.assertEquals(character.strength, 0)
        self.assertEquals(character.constitution, 0)
        self.assertEquals(character.dexterity, 0)
        self.assertEquals(character.intelligence, 0)
        self.assertEquals(character.wisdom, 0)
        self.assertEquals(character.charisma, 0)

    def test_create_character_with_ability_score(self):
        self.character_gateway.set_ability_score(10, 10, 10, 10, 10, 10)
        self.character_gateway.race_gateway = self.race_gateway
        character = self.character_gateway.create_character()

        self.assertEquals(character.strength, 10)
        self.assertEquals(character.constitution, 10)
        self.assertEquals(character.dexterity, 10)
        self.assertEquals(character.intelligence, 10)
        self.assertEquals(character.wisdom, 10)
        self.assertEquals(character.charisma, 10)

    def test_create_character_with_ability_score_and_racial_bonus(self):
        self.character_gateway.set_ability_score(10, 10, 10, 10, 10, 10)
        self.race_gateway.set_ability_score(2, 0, 2, 0, 2, 0)
        self.character_gateway.race_gateway = self.race_gateway
        character = self.character_gateway.create_character()

        self.assertEquals(character.strength, 12)
        self.assertEquals(character.constitution, 10)
        self.assertEquals(character.dexterity, 12)
        self.assertEquals(character.intelligence, 10)
        self.assertEquals(character.wisdom, 12)
        self.assertEquals(character.charisma, 10)

    def test_create_elf_race_character(self):
        self.character_gateway.set_ability_score(10, 10, 10, 10, 10, 10)
        race_gateway = ElfRaceGateway()
        character = CreateCharacterUsecase(self.character_gateway, race_gateway).execute()

        self.assertEquals(character.strength, 10)
        self.assertEquals(character.constitution, 10)
        self.assertEquals(character.dexterity, 12)
        self.assertEquals(character.intelligence, 10)
        self.assertEquals(character.wisdom, 12)
        self.assertEquals(character.charisma, 10)

    def test_create_dwarf_race_character(self):
        self.character_gateway.set_ability_score(10, 10, 10, 10, 10, 10)
        race_gateway = DwarfRaceGateway()
        character = CreateCharacterUsecase(self.character_gateway, race_gateway).execute()

        self.assertEquals(character.strength, 10)
        self.assertEquals(character.constitution, 12)
        self.assertEquals(character.dexterity, 10)
        self.assertEquals(character.intelligence, 10)
        self.assertEquals(character.wisdom, 12)
        self.assertEquals(character.charisma, 10)
