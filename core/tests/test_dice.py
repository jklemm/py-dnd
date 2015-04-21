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


class RollTheNormalDiceTests(RollTheDiceTestCase):

    def test_roll_a_dice_with_four_sides(self):
        result = self.roll_the_dice_with_formula('d4')
        self.assertLimits(result, 1, 4)

    def test_roll_a_dice_with_six_sides(self):
        result = self.roll_the_dice_with_formula('d6')
        self.assertLimits(result, 1, 6)

    def test_roll_a_dice_with_eight_sides(self):
        result = self.roll_the_dice_with_formula('d8')
        self.assertLimits(result, 1, 8)

    def test_roll_a_dice_with_twelve_sides(self):
        result = self.roll_the_dice_with_formula('d12')
        self.assertLimits(result, 1, 12)

    def test_roll_a_dice_with_twenty_sides(self):
        result = self.roll_the_dice_with_formula('d20')
        self.assertLimits(result, 1, 20)


class RollTheDiceTwiceTests(RollTheDiceTestCase):

    def test_roll_twice_the_dice(self):
        result = self.roll_the_dice_with_formula('2d4')
        self.assertLimits(result, 2, 8)

        result = self.roll_the_dice_with_formula('2d6')
        self.assertLimits(result, 2, 12)

        result = self.roll_the_dice_with_formula('2d8')
        self.assertLimits(result, 2, 16)

        result = self.roll_the_dice_with_formula('2d10')
        self.assertLimits(result, 2, 20)

        result = self.roll_the_dice_with_formula('2d12')
        self.assertLimits(result, 2, 24)

        result = self.roll_the_dice_with_formula('2d20')
        self.assertLimits(result, 2, 40)

    def test_roll_three_times_the_dice(self):
        result = self.roll_the_dice_with_formula('3d4')
        self.assertLimits(result, 3, 12)

        result = self.roll_the_dice_with_formula('3d6')
        self.assertLimits(result, 3, 18)

        result = self.roll_the_dice_with_formula('3d8')
        self.assertLimits(result, 3, 24)

        result = self.roll_the_dice_with_formula('3d10')
        self.assertLimits(result, 3, 30)

        result = self.roll_the_dice_with_formula('3d12')
        self.assertLimits(result, 3, 36)

        result = self.roll_the_dice_with_formula('3d20')
        self.assertLimits(result, 3, 60)


class RollTheDiceMultipleTimesWithBonusTests(RollTheDiceTestCase):

    def test_roll_multiple_times_with_bonus(self):
        result = self.roll_the_dice_with_formula('2d4+4')
        self.assertLimits(result, 6, 12)

        result = self.roll_the_dice_with_formula('3d6+8')
        self.assertLimits(result, 11, 26)

        result = self.roll_the_dice_with_formula('4d8+12')
        self.assertLimits(result, 16, 44)

        result = self.roll_the_dice_with_formula('5d10+16')
        self.assertLimits(result, 17, 66)

        result = self.roll_the_dice_with_formula('6d12+20')
        self.assertLimits(result, 26, 92)

        result = self.roll_the_dice_with_formula('7d20+24')
        self.assertLimits(result, 31, 164)


class RollTheCustomDiceMultipleTimesWithBonusTests(RollTheDiceTestCase):

    def test_roll_custom_dice(self):
        result = self.roll_the_dice_with_formula('142d271+43')
        self.assertLimits(result, 185, 38525)

        result = self.roll_the_dice_with_formula('20d1000+32')
        self.assertLimits(result, 52, 20032)

        result = self.roll_the_dice_with_formula('379d6523+641')
        self.assertLimits(result, 379, 2472858)
