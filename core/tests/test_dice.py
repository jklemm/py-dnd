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

    def verify_dice_result_rolls(self, tests):
        for (formula, minimum, maximum) in tests:
            result = self.roll_the_dice_with_formula(formula)
            self.assertLimits(result, minimum, maximum)


class RollSimpleDiceTests(RollTheDiceTestCase):

    def test_roll_a_dice_with_default_sides(self):
        result = Dice().roll()
        self.assertLimits(result, 1, 4)

    def test_roll_a_dice_with_none_side(self):
        result = self.roll_the_dice_with_sides(None)
        self.assertLimits(result, 1, 4)

    def test_roll_a_dice_with_four_sides(self):
        result = self.roll_the_dice_with_sides(4)
        self.assertLimits(result, 1, 4)

    def test_roll_a_dice_with_six_sides(self):
        result = self.roll_the_dice_with_sides(6)
        self.assertLimits(result, 1, 6)

    def test_roll_a_dice_with_eight_sides(self):
        result = self.roll_the_dice_with_sides(8)
        self.assertLimits(result, 1, 8)

    def test_roll_a_dice_with_ten_sides(self):
        result = self.roll_the_dice_with_sides(10)
        self.assertLimits(result, 1, 10)

    def test_roll_a_dice_with_twelve_sides(self):
        result = self.roll_the_dice_with_sides(12)
        self.assertLimits(result, 1, 12)

    def test_roll_a_dice_with_twenty_sides(self):
        result = self.roll_the_dice_with_sides(20)
        self.assertLimits(result, 1, 20)


class RollTheDiceTests(RollTheDiceTestCase):

    def test_roll_normal_dices(self):
        tests = (('d4', 1, 4), ('d6', 1, 6), ('d8', 1, 8), ('d12', 1, 12), ('d20', 1, 20))
        self.verify_dice_result_rolls(tests)

    def test_roll_twice_the_dice(self):
        tests = (('2d4', 2, 8), ('2d6', 2, 12), ('2d8', 2, 16), ('2d10', 2, 20), ('2d12', 2, 24), ('2d20', 2, 40))
        self.verify_dice_result_rolls(tests)

    def test_roll_three_times_the_dice(self):
        tests = (('3d4', 3, 12), ('3d6', 3, 18), ('3d8', 3, 24), ('3d10', 3, 30), ('3d12', 3, 36), ('3d20', 3, 60))
        self.verify_dice_result_rolls(tests)

    def test_roll_multiple_times_with_bonus(self):
        tests = (('2d4+4', 6, 12), ('3d6+8', 11, 26), ('4d8+12', 16, 44), ('5d10+16', 21, 66), ('6d12+20', 26, 92))
        self.verify_dice_result_rolls(tests)

    def test_roll_custom_dice(self):
        tests = (('142d271+43', 185, 38525), ('20d1000+32', 52, 20032), ('379d6523+641', 379, 2472858))
        self.verify_dice_result_rolls(tests)
