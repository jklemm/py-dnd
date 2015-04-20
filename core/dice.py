#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint
import re


class Dice():

    def __init__(self, sides=4):
        self.sides = self._get_dice_sides(sides)

    def _get_dice_sides(self, sides=None):
        return sides if sides and sides >= 4 else 4

    def roll(self):
        return randint(1, self.sides)


class DiceRoller():

    def __init__(self, d20_formula):
        self.dice = None
        self.times = 1
        self.bonus = 0
        self.slice_formula(d20_formula)

    def slice_formula(self, formula):
        regex = re.compile(r'(\d+)*d(\d+)*[+]*(\d+)*')
        result_regex = re.match(regex, formula)
        if result_regex:
            try:
                self.times = int(result_regex.group(1))
            except (TypeError, ValueError):
                self.times = 1

            try:
                sides = int(result_regex.group(1))
            except (TypeError, ValueError):
                self.dice = Dice()
            else:
                self.dice = Dice(sides)

            try:
                self.bonus = int(result_regex.group(3))
            except (TypeError, ValueError):
                self.bonus = 0

    def roll(self):
        result = 0
        for i in range(0, self.times):
            result += self.dice.roll()
        return result + self.bonus
