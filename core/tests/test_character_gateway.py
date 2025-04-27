from unittest import TestCase
from core.gateways.character_gateway import CharacterGateway
from core.entities.dwarf_race_entity import DwarfRaceEntity
from core.entities.elf_race_entity import ElfRaceEntity
from core.entities.default_race_entity import DefaultRaceEntity
from core.structs.character_struct import CharacterStruct


class CharacterGatewayTests(TestCase):
    def setUp(self):
        self.character_gateway = CharacterGateway()
        self.race_entity = DefaultRaceEntity()

    def test_not_none(self):
        character = self.character_gateway.create_character()
        self.assertIsNotNone(character)
        self.assertIsInstance(character, CharacterStruct)

    def test_create_an_empty_character(self):
        self.character_gateway.race_entity = self.race_entity
        character = self.character_gateway.create_character()

        self._assertAbilityScore(character, 0, 0, 0, 0, 0, 0)

    def test_create_character_with_ability_score(self):
        self.character_gateway.set_ability_score(10, 10, 10, 10, 10, 10)
        self.character_gateway.race_entity = self.race_entity
        character = self.character_gateway.create_character()

        self._assertAbilityScore(character, 10, 10, 10, 10, 10, 10)

    def test_create_character_with_ability_score_and_racial_bonus(self):
        self.character_gateway.set_ability_score(10, 10, 10, 10, 10, 10)
        self.race_entity.set_ability_score(2, 0, 2, 0, 2, 0)
        self.character_gateway.race_entity = self.race_entity
        character = self.character_gateway.create_character()

        self._assertAbilityScore(character, 12, 10, 12, 10, 12, 10)

    def test_create_elf_race_character(self):
        self.character_gateway.set_ability_score(10, 10, 10, 10, 10, 10)
        self.character_gateway.race_entity = ElfRaceEntity()
        character = self.character_gateway.create_character()

        self._assertAbilityScore(character, 10, 10, 12, 10, 12, 10)

    def test_create_dwarf_race_character(self):
        self.character_gateway.set_ability_score(10, 10, 10, 10, 10, 10)
        self.character_gateway.race_entity = DwarfRaceEntity()
        character = self.character_gateway.create_character()

        self._assertAbilityScore(character, 10, 12, 10, 10, 12, 10)

    def _assertAbilityScore(self, character, strength, constitution, dexterity, intelligence, wisdom, charisma):
        self.assertEqual(character.strength, strength)
        self.assertEqual(character.constitution, constitution)
        self.assertEqual(character.dexterity, dexterity)
        self.assertEqual(character.intelligence, intelligence)
        self.assertEqual(character.wisdom, wisdom)
        self.assertEqual(character.charisma, charisma)
