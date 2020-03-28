from unittest import TestCase
from core.utils import Dice, DiceRoller


class DiceSidesTests(TestCase):

    def setUp(self):
        self.dice = Dice()

    def test_dice_with_default_side(self):
        self.assertEqual(self.dice.sides, 4)

    def test_dice_with_none_sides(self):
        self.dice.set_sides(None)
        self.assertEqual(self.dice.sides, 4)

    def test_dice_with_two_sides(self):
        self.dice.set_sides(2)
        self.assertEqual(self.dice.sides, 4)

    def test_dice_with_four_sides(self):
        self.dice.set_sides(4)
        self.assertEqual(self.dice.sides, 4)

    def test_dice_with_six_sides(self):
        self.dice.set_sides(6)
        self.assertEqual(self.dice.sides, 6)


class RollTheDiceTestCase(TestCase):

    def roll_the_dice(self, sides):
        return Dice(sides).roll()

    def dice_roller_roll_the_dice(self, formula):
        return DiceRoller(formula).roll()

    def assertLimits(self, value, minimum, maximum):
        self.assertGreaterEqual(value, minimum)
        self.assertLessEqual(value, maximum)

    def assertSideDiceResults(self, sides):
        result = self.roll_the_dice(sides)
        self.assertLimits(result, 1, sides)

    def assertFormulaDiceResults(self, formula, minimum_result, maximum_result):
        result = self.dice_roller_roll_the_dice(formula)
        self.assertLimits(result, minimum_result, maximum_result)


class RollSimpleDiceTests(RollTheDiceTestCase):

    def test_roll_a_dice_with_d20_sides(self):
        self.assertSideDiceResults(4)
        self.assertSideDiceResults(6)
        self.assertSideDiceResults(8)
        self.assertSideDiceResults(10)
        self.assertSideDiceResults(12)
        self.assertSideDiceResults(20)


class RollComplexDiceTests(RollTheDiceTestCase):

    def test_roll_normal_dices(self):
        self.assertFormulaDiceResults('d4', 1, 4)
        self.assertFormulaDiceResults('d6', 1, 6)
        self.assertFormulaDiceResults('d8', 1, 8)
        self.assertFormulaDiceResults('d12', 1, 12)
        self.assertFormulaDiceResults('d20', 1, 20)

    def test_roll_twice_the_dice(self):
        self.assertFormulaDiceResults('2d4', 2, 8)
        self.assertFormulaDiceResults('2d6', 2, 12)
        self.assertFormulaDiceResults('2d8', 2, 16)
        self.assertFormulaDiceResults('2d10', 2, 20)
        self.assertFormulaDiceResults('2d12', 2, 24)
        self.assertFormulaDiceResults('2d20', 2, 40)

    def test_roll_three_times_the_dice(self):
        self.assertFormulaDiceResults('3d4', 3, 12)
        self.assertFormulaDiceResults('3d6', 3, 18)
        self.assertFormulaDiceResults('3d8', 3, 24)
        self.assertFormulaDiceResults('3d10', 3, 30)
        self.assertFormulaDiceResults('3d12', 3, 36)
        self.assertFormulaDiceResults('3d20', 3, 60)

    def test_roll_four_times_with_bonus(self):
        self.assertFormulaDiceResults('4d4+4', 8, 20)
        self.assertFormulaDiceResults('4d6+4', 8, 28)
        self.assertFormulaDiceResults('4d8+4', 8, 36)
        self.assertFormulaDiceResults('4d10+4', 8, 44)
        self.assertFormulaDiceResults('4d12+4', 8, 52)
        self.assertFormulaDiceResults('4d20+4', 8, 84)

    def test_roll_custom_dice(self):
        self.assertFormulaDiceResults('10d10+20', 30, 120)
        self.assertFormulaDiceResults('10d20+20', 30, 220)
        self.assertFormulaDiceResults('10d30+20', 30, 320)
        self.assertFormulaDiceResults('10d40+20', 30, 420)
        self.assertFormulaDiceResults('10d50+20', 30, 520)
        self.assertFormulaDiceResults('10d60+20', 30, 620)
