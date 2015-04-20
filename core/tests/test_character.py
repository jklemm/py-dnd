#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest


class CharacterStruct(object):

    def __init__(self):
        self.strength = 0
        self.constitution = 0
        self.dexterity = 0
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 0


class CharacterGateway(object):

    def create_character(self):
        return CharacterStruct()


class CreateCharacterUsecase():

    def __init__(self, character_gateway):
        self.character_gateway = character_gateway

    def execute(self):
        return self.character_gateway.create_character()


class CreateCharacterUsecaseTests(unittest.TestCase):

    def test_create_empty_character(self):
        character_gateway = CharacterGateway()
        usecase = CreateCharacterUsecase(character_gateway)
        character = usecase.execute()

        self.assertIsNotNone(character)
        self.assertIsInstance(character, CharacterStruct)

    def test_create_character_with_ability_scores(self):
        character_gateway = CharacterGateway()
        usecase = CreateCharacterUsecase(character_gateway)
        character = usecase.execute()

        self.assertTrue(hasattr(character, 'strength'))
        self.assertTrue(hasattr(character, 'constitution'))
        self.assertTrue(hasattr(character, 'dexterity'))
        self.assertTrue(hasattr(character, 'intelligence'))
        self.assertTrue(hasattr(character, 'wisdom'))
        self.assertTrue(hasattr(character, 'charisma'))

    def test_create_elf_race_character(self):

