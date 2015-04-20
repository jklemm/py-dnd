#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint
import re


class Dice():

    def __init__(self, lados=4):
        self.lados = lados

    def jogar(self):
        return randint(1, self.lados)


class JogadorDeDados():

    def __init__(self, formula_d20):
        self.dado = None
        self.vezes = 1
        self.bonus = 0
        self.recortar_formula(formula_d20)

    def recortar_formula(self, formula):
        regex = re.compile(r'(\d+)*d(\d+)*[+]*(\d+)*')
        result_regex = re.match(regex, formula)
        if result_regex:
            try:
                self.vezes = int(result_regex.group(1))
            except (TypeError, ValueError):
                self.vezes = 1

            try:
                lados = int(result_regex.group(1))
            except (TypeError, ValueError):
                self.dado = Dice()
            else:
                self.dado = Dice(lados)

            try:
                self.bonus = int(result_regex.group(3))
            except (TypeError, ValueError):
                self.bonus = 0

    def jogar(self):
        resultado = 0
        for i in range(0, self.vezes):
            resultado += self.dado.jogar()
        return resultado + self.bonus
