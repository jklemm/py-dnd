from unittest import TestCase
from core.structs.character_struct import CharacterStruct
from core.usecases.create_character_usecase import CreateCharacterUsecase
from core.gateways.character_gateway import CharacterGateway


class CreateCharacterUsecaseTests(TestCase):
    def test_not_none(self):
        character_gateway = CharacterGateway()
        character = CreateCharacterUsecase(character_gateway).execute()

        self.assertIsNotNone(character)
        self.assertIsInstance(character, CharacterStruct)
