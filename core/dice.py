#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint
import re


class Dice():

    def __init__(self, sides=4):
        self.sides = sides

    def throw(self):
        return randint(1, self.sides)


class DiceThrower():

    def __init__(self, dice_formula):
        self.dice = None
        self.times = 1
        self.bonus = 0
        self.slice_formula(dice_formula)

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

    def throw(self):
        result = 0
        for i in range(0, self.times):
            result += self.dice.throw()
        return result + self.bonus
