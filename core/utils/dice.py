#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint
import re


class Dice():

    def __init__(self, sides=4):
        self.sides = 4

    def set_sides(self, sides):
        if sides is not None and sides > 4:
            self.sides = sides

    def roll(self):
        return randint(1, self.sides)


class DiceRoller():

    def __init__(self, d20_formula):
        self.dice = Dice()
        self.times = 1
        self.bonus = 0
        self.slice_formula(d20_formula)

    def slice_formula(self, formula):
        regex = re.compile(r'(\d+)*d(\d+)*[+]*(\d+)*')
        result_regex = re.match(regex, formula)
        if result_regex:
            times = self.get_integer_value(result_regex, 1)
            sides = self.get_integer_value(result_regex, 2)
            bonus = self.get_integer_value(result_regex, 3)
            self.times = times or 1
            self.dice.set_sides(sides)
            self.bonus = bonus

    def get_integer_value(self, result_regex, group_index):
        value = 0
        try:
            value = int(result_regex.group(group_index))
        except (TypeError, ValueError):
            pass
        return value

    def roll(self):
        result = 0
        for i in range(0, self.times):
            result += self.dice.roll()
        return result + self.bonus
