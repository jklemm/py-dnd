#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from core.dice import DiceThrower
from dice import Dice


class DiceTest(unittest.TestCase):

    def test__one_side_throw(self):
        sides = 1
        result = self._create_and_throw_dice(sides)
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 4)

    def test__four_sides_throw(self):
        sides = 4
        result = self._create_and_throw_dice(sides)
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, sides)

    def test__six_sides_throw(self):
        sides = 6
        result = self._create_and_throw_dice(sides)
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, sides)

    def _create_and_throw_dice(self, sides):
        return Dice(sides).throw()


class NormalThrowDiceTest(unittest.TestCase):

    def test__d4(self):
        result = DiceThrower('d4').throw()
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 4)

    def test__d6(self):
        result = DiceThrower('d6').throw()
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 6)

    def test__d8(self):
        result = DiceThrower('d8').throw()
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 8)

    def test__d12(self):
        result = DiceThrower('d12').throw()
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 12)

    def test__d20(self):
        result = DiceThrower('d20').throw()
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 20)


class MultipleTimesDiceTest(unittest.TestCase):

    def test__2d12(self):
        result = DiceThrower('2d12').throw()
        self.assertGreaterEqual(result, 2)
        self.assertLessEqual(result, 24)

    def test__3d20(self):
        result = DiceThrower('3d20').throw()
        self.assertGreaterEqual(result, 3)
        self.assertLessEqual(result, 60)


class MultipleTimesWithBonusDiceTest(unittest.TestCase):

    def test__2d20_plus_10(self):
        result = DiceThrower('2d20+10').throw()
        self.assertGreaterEqual(result, 12)
        self.assertLessEqual(result, 50)

    def test__3d8_plus_4(self):
        result = DiceThrower('3d8+4').throw()
        self.assertGreaterEqual(result, 7)
        self.assertLessEqual(result, 28)


class CustomDiceTest(unittest.TestCase):

    def test__3d1000_plus_20(self):
        result = DiceThrower('3d1000+20').throw()
        self.assertGreaterEqual(result, 23)
        self.assertLessEqual(result, 3020)
