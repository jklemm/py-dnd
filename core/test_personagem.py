#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from core.personagem import Personagem


class CriarPersonagemUsecase():
    
    def __init__(self):
        pass

    def execute(self):
        return Personagem()


class CriarPersonagemUsecaseTests(unittest.TestCase):

    def test__criar_um_personagem_vazio(self):
        usecase = CriarPersonagemUsecase()
        personagem = usecase.execute()

        self.assertIsNotNone(personagem)
        self.assertIsInstance(personagem, Personagem)

    def test__criar_um_personagem_com_atributos(self):
        usecase = CriarPersonagemUsecase()
        personagem = usecase.execute()

        self.assertEquals(personagem.forca, 0)
        self.assertEquals(personagem.destreza, 0)
        self.assertEquals(personagem.constituicao, 0)
        self.assertEquals(personagem.sabedoria, 0)
        self.assertEquals(personagem.inteligencia, 0)
        self.assertEquals(personagem.carisma, 0)
