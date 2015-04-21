#!/usr/bin/python

from unittest import TestCase
from core.dice import Dice, DiceRoller


class DiceSidesTests(TestCase):

    def test_dice_with_default_side(self):
        self.assertEquals(Dice().sides, 4)

    def test_dice_with_none_sides(self):
        self.assertEquals(Dice(None).sides, 4)

    def test_dice_with_two_sides(self):
        self.assertEquals(Dice(2).sides, 4)

    def test_dice_with_four_sides(self):
        self.assertEquals(Dice(4).sides, 4)

    def test_dice_with_twelve_sides(self):
        self.assertEquals(Dice(12).sides, 12)


class RollSimpleDiceTests(TestCase):

    def test_roll_a_dice_with_default_sides(self):
        result = Dice().roll()
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 4)

    def test_roll_a_dice_with_none_side(self):
        result = Dice(None).roll()
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 4)

    def test_roll_a_dice_with_four_sides(self):
        result = Dice(4).roll()
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 4)

    def test_roll_a_dice_with_six_sides(self):
        result = Dice(6).roll()
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 6)

    def test_roll_a_dice_with_eight_sides(self):
        result = Dice(8).roll()
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 8)

    def test_roll_a_dice_with_ten_sides(self):
        result = Dice(10).roll()
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 10)

    def test_roll_a_dice_with_twelve_sides(self):
        result = Dice(12).roll()
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 12)

    def test_roll_a_dice_with_twenty_sides(self):
        result = Dice(20).roll()
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 20)


class RollTheNormalDiceTests(TestCase):

    def test_roll_a_dice_with_four_sides(self):
        result = DiceRoller('d4').roll()
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 4)

    def test_roll_a_dice_with_six_sides(self):
        result = DiceRoller('d6').roll()
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 6)

    def test_roll_a_dice_with_eight_sides(self):
        result = DiceRoller('d8').roll()
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 8)

    def test_roll_a_dice_with_twelve_sides(self):
        result = DiceRoller('d12').roll()
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 12)

    def test_roll_a_dice_with_twenty_sides(self):
        result = DiceRoller('d20').roll()
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 20)


class RollTheDiceTwiceTests(TestCase):

    def test_roll_twice_a_four_sides_dice(self):
        result = DiceRoller('2d4').roll()
        self.assertGreaterEqual(result, 2)
        self.assertLessEqual(result, 8)

    def test_roll_twice_a_six_sides_dice(self):
        result = DiceRoller('2d6').roll()
        self.assertGreaterEqual(result, 2)
        self.assertLessEqual(result, 12)

    def test_roll_twice_an_eight_sides_dice(self):
        result = DiceRoller('2d8').roll()
        self.assertGreaterEqual(result, 2)
        self.assertLessEqual(result, 12)

    def test_roll_twice_a_ten_sides_dice(self):
        result = DiceRoller('2d10').roll()
        self.assertGreaterEqual(result, 2)
        self.assertLessEqual(result, 20)

    def test_roll_twice_a_twelve_sides_dice(self):
        result = DiceRoller('2d12').roll()
        self.assertGreaterEqual(result, 2)
        self.assertLessEqual(result, 24)

    def test_roll_twice_a_twenty_sides_dice(self):
        result = DiceRoller('2d20').roll()
        self.assertGreaterEqual(result, 2)
        self.assertLessEqual(result, 40)


class RollTheDiceThreeTimesTests(TestCase):

    def test_roll_three_times_a_four_sides_dice(self):
        result = DiceRoller('3d4').roll()
        self.assertGreaterEqual(result, 3)
        self.assertLessEqual(result, 12)

    def test_roll_three_times_a_six_sides_dice(self):
        result = DiceRoller('3d6').roll()
        self.assertGreaterEqual(result, 3)
        self.assertLessEqual(result, 18)

    def test_roll_three_times_an_eight_sides_dice(self):
        result = DiceRoller('3d8').roll()
        self.assertGreaterEqual(result, 3)
        self.assertLessEqual(result, 24)

    def test_roll_three_times_a_ten_sides_dice(self):
        result = DiceRoller('3d10').roll()
        self.assertGreaterEqual(result, 3)
        self.assertLessEqual(result, 30)

    def test_roll_three_times_a_twelve_sides_dice(self):
        result = DiceRoller('3d12').roll()
        self.assertGreaterEqual(result, 3)
        self.assertLessEqual(result, 36)

    def test_roll_three_times_a_twenty_sides_dice(self):
        result = DiceRoller('3d20').roll()
        self.assertGreaterEqual(result, 3)
        self.assertLessEqual(result, 60)


class RollTheDiceMultipleTimesWithBonusTests(TestCase):

    def test_roll_2d4_plus_4(self):
        result = DiceRoller('2d4+4').roll()
        self.assertGreaterEqual(result, 6)
        self.assertLessEqual(result, 12)

    def test_roll_3d6_plus_8(self):
        result = DiceRoller('3d6+8').roll()
        self.assertGreaterEqual(result, 11)
        self.assertLessEqual(result, 26)

    def test_roll_4d8_plus_12(self):
        result = DiceRoller('4d8+12').roll()
        self.assertGreaterEqual(result, 16)
        self.assertLessEqual(result, 44)

    def test_roll_5d10_plus_16(self):
        result = DiceRoller('5d10+16').roll()
        self.assertGreaterEqual(result, 17)
        self.assertLessEqual(result, 66)

    def test_roll_6d12_plus_20(self):
        result = DiceRoller('6d12+20').roll()
        self.assertGreaterEqual(result, 26)
        self.assertLessEqual(result, 92)

    def test_roll_7d20_plus_24(self):
        result = DiceRoller('7d20+24').roll()
        self.assertGreaterEqual(result, 31)
        self.assertLessEqual(result, 164)


class RollTheCustomDiceMultipleTimesWithBonusTests(TestCase):

    def test_roll_142d271_plus_43(self):
        result = DiceRoller('142d271+43').roll()
        self.assertGreaterEqual(result, 185)
        self.assertLessEqual(result, 38525)

    def test_roll_20d1000_plus_32(self):
        result = DiceRoller('20d1000+32').roll()
        self.assertGreaterEqual(result, 52)
        self.assertLessEqual(result, 20032)

    def test_roll_379d6523_plus_641(self):
        result = DiceRoller('379d6523+641').roll()
        self.assertGreaterEqual(result, 379)
        self.assertLessEqual(result, 2472858)
