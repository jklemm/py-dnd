#!/usr/bin/python

import logging, sys
import unittest
from classes.dice import *

FORMAT = '%(levelname)s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG)
log = logging.getLogger()

class DiceTestCase(unittest.TestCase):

	def setUp(self):
		pass

	# Normal dices
	def test_d4(self):
		for i in range(1,6):
			if i == 1 and log.isEnabledFor(logging.DEBUG):
				print ""
			result = Dice("d4").throwDice()
			log.debug("test %d | d4 -> %d", i, result)
			self.assertGreaterEqual(result, 1)
			self.assertLessEqual(result, 4)

	def test_d6(self):
		for i in range(1,6):
			if i == 1 and log.isEnabledFor(logging.DEBUG):
				print ""
			result = Dice("d6").throwDice()
			log.debug("test %d | d6 -> %d", i, result)
			self.assertGreaterEqual(result, 1)
			self.assertLessEqual(result, 6)

	def test_d8(self):
		for i in range(1,6):
			if i == 1 and log.isEnabledFor(logging.DEBUG):
				print ""
			result = Dice("d8").throwDice()
			log.debug("test %d | d8 -> %d", i, result)
			self.assertGreaterEqual(result, 1)
			self.assertLessEqual(result, 8)

	def test_d12(self):
		for i in range(1,6):
			if i == 1 and log.isEnabledFor(logging.DEBUG):
				print ""
			result = Dice("d12").throwDice()
			log.debug("test %d | d12 -> %d", i, result)
			self.assertGreaterEqual(result, 1)
			self.assertLessEqual(result, 12)

	def test_d20(self):
		for i in range(1,6):
			if i == 1 and log.isEnabledFor(logging.DEBUG):
				print ""
			result = Dice("d20").throwDice()
			log.debug("test %d | d20 -> %d", i, result)
			self.assertGreaterEqual(result, 1)
			self.assertLessEqual(result, 20)

	# Manual Tests with Times
	def test_2d12(self):
		for i in range(1,6):
			if i == 1 and log.isEnabledFor(logging.DEBUG):
				print ""
			result = Dice("2d12").throwDice()
			log.debug("test %d | 2d12 -> %d", i, result)
			self.assertGreaterEqual(result, 2)
			self.assertLessEqual(result, 24)

	def test_3d20(self):
		for i in range(1,6):
			if i == 1 and log.isEnabledFor(logging.DEBUG):
				print ""
			result = Dice("3d20").throwDice()
			log.debug("test %d | 3d20 -> %d", i, result)
			self.assertGreaterEqual(result, 3)
			self.assertLessEqual(result, 60)

	# Manual Tests with Times and Bonus
	def test_2d20plus10(self):
		for i in range(1,6):
			if i == 1 and log.isEnabledFor(logging.DEBUG):
				print ""
			result = Dice("2d20+10").throwDice()
			log.debug("test %d | 2d20+10 -> %d", i, result)
			self.assertGreaterEqual(result, 12)
			self.assertLessEqual(result, 50)

	def test_3d8plus4(self):
		for i in range(1,6):
			if i == 1 and log.isEnabledFor(logging.DEBUG):
				print ""
			result = Dice("3d8+4").throwDice()
			log.debug("test %d | 3d8+4 -> %d", i, result)
			self.assertGreaterEqual(result, 7)
			self.assertLessEqual(result, 28)

	# Manual Tests with custom side Dice
	def test_3d1000plus20(self):
		for i in range(1,6):
			if i == 1 and log.isEnabledFor(logging.DEBUG):
				print ""
			result = Dice("3d1000+20").throwDice()
			log.debug("test %d | 3d1000+20 -> %d", i, result)
			self.assertGreaterEqual(result, 23)
			self.assertLessEqual(result, 3020)

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(DiceTestCase)
	unittest.TextTestRunner(verbosity=1).run(suite)
