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
            self.set_times(result_regex.group(1))
            self.set_dice_sides(result_regex.group(2))
            self.set_roll_bonus(result_regex.group(3))

    def set_times(self, times):
        try:
            self.times = int(times)
        except (TypeError, ValueError):
            pass

    def set_dice_sides(self, number_of_sides):
        try:
            sides = int(number_of_sides)
            self.dice.set_sides(sides)
        except (TypeError, ValueError):
            pass

    def set_roll_bonus(self, bonus):
        try:
            self.bonus = int(bonus)
        except (TypeError, ValueError):
            pass

    def roll(self):
        result = 0
        for i in range(0, self.times):
            result += self.dice.roll()
        return result + self.bonus
