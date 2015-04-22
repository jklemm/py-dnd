#!/usr/bin/python
from unittest import TestCase
from core.utils.dice import Dice, DiceRoller


class DiceSidesTests(TestCase):

    def setUp(self):
        self.dice = Dice()

    def test_dice_with_default_side(self):
        self.assertEquals(self.dice.sides, 4)

    def test_dice_with_none_sides(self):
        self.dice.set_sides(None)
        self.assertEquals(self.dice.sides, 4)

    def test_dice_with_two_sides(self):
        self.dice.set_sides(2)
        self.assertEquals(self.dice.sides, 4)

    def test_dice_with_four_sides(self):
        self.dice.set_sides(4)
        self.assertEquals(self.dice.sides, 4)

    def test_dice_with_six_sides(self):
        self.dice.set_sides(6)
        self.assertEquals(self.dice.sides, 6)


class RollTheDiceTestCase(TestCase):

    def roll_the_dice_with_sides(self, sides):
        return Dice(sides).roll()

    def roll_the_dice_with_formula(self, formula):
        return DiceRoller(formula).roll()

    def assertLimits(self, value, minimum, maximum):
        self.assertGreaterEqual(value, minimum)
        self.assertLessEqual(value, maximum)

    def assertSideDiceResults(self, test_list):
        for sides in test_list:
            result = self.roll_the_dice_with_sides(sides)
            self.assertLimits(result, 1, sides)

    def assertFormulaDiceResults(self, test_list, minimum_result):
        for (formula, maximum_result) in test_list:
            result = self.roll_the_dice_with_formula(formula)
            self.assertLimits(result, minimum_result, maximum_result)


class RollSimpleDiceTests(RollTheDiceTestCase):

    def test_roll_a_dice_with_d20_sides(self):
        tests = (4, 6, 8, 12, 20)
        self.assertSideDiceResults(tests)


class RollComplexDiceTests(RollTheDiceTestCase):

    def test_roll_normal_dices(self):
        tests = (('d4', 4), ('d6', 6), ('d8', 8), ('d12', 12), ('d20', 20))
        self.assertFormulaDiceResults(tests, 1)

    def test_roll_twice_the_dice(self):
        tests = (('2d4', 8), ('2d6', 12), ('2d8', 16), ('2d10', 20), ('2d12', 24), ('2d20', 40))
        self.assertFormulaDiceResults(tests, 2)

    def test_roll_three_times_the_dice(self):
        tests = (('3d4', 12), ('3d6', 18), ('3d8', 24), ('3d10', 30), ('3d12', 36), ('3d20', 60))
        self.assertFormulaDiceResults(tests, 3)

    def test_roll_four_times_with_bonus(self):
        tests = (('4d4+4', 20), ('4d6+4', 28), ('4d8+4', 36), ('4d10+4', 44), ('4d12+4', 52))
        self.assertFormulaDiceResults(tests, 8)

    def test_roll_custom_dice(self):
        tests = (('10d30+20', 320), ('10d40+20', 420), ('10d50+20', 520), ('10d60+20', 620))
        self.assertFormulaDiceResults(tests, 30)
