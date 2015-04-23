from unittest import TestCase
from core.structs import CharacterStruct
from core.usecases import CreateCharacterUsecase
from core.gateways import CharacterGateway


class CreateCharacterUsecaseTests(TestCase):
    def test_not_none(self):
        character_gateway = CharacterGateway()
        character = CreateCharacterUsecase(character_gateway).execute()

        self.assertIsNotNone(character)
        self.assertIsInstance(character, CharacterStruct)
