
from random import randint
import re
import logging

class Dice(object):

	def __init__ (self, formula):
		self.times = 1
		self.sides = 0
		self.bonus = 0
		self.sliceFormula(formula)

	def sliceFormula(self, formula):
		regexp = re.compile(r'(\d+)*d(\d+)*[+]*(\d+)*')
		m = re.match(regexp, formula)
		if m:
			try:
				self.times = int(m.group(1))
			except:
				self.times = 1

			try:
				self.sides = int(m.group(2))
			except:
				self.sides = 4 # the minimum sides of a dice

			try:
				self.bonus = int(m.group(3))
			except:
				self.bonus = 0

	def throwDice(self):
		result = 0
		for i in range(0,self.times):
			randomnumber = randint(1,self.sides)
			logging.debug (str(randomnumber) + " + ")
			result += randomnumber
		logging.debug (str(self.bonus) + " = ")
		return result + self.bonus

# Manual Tests simple side dice
#print (Dice("d4").throwDice())
#print (Dice("d6").throwDice())
#print (Dice("d8").throwDice())
#print (Dice("d12").throwDice())
#print (Dice("d20").throwDice())

# Manual Tests with Times
#print (Dice("2d12").throwDice())
#print (Dice("3d20").throwDice())

# Manual Tests with Times and Bonus
#print (Dice("2d20+10").throwDice())
#print (Dice("3d8+4").throwDice())

# Manual Tests with custom side Dice
#print (Dice("3d1000+20").throwDice())