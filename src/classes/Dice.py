
from random import randint

class Dice(object):

	def __init__ (self, formula):
		self.times = 0
		self.sides = 0
		self.bonus = 0
		self.sliceFormula(formula)

	def sliceFormula(self, formula):
		array = formula.partition('d')
		try:
			self.times = int(array[0])
		except:
			self.times = 1
		waste = array[2]
		waste = waste.partition('+')
		try:
			self.sides = int(waste[0])
		except:
			self.sides = 4 # the minimum sides of a dice
		try:
			self.bonus = int(waste[2])
		except:
			self.bonus = 0

	def throwDice(self):
		result = 0
		for i in range(0,self.times):
			randomnumber = randint(1,self.sides)
			print (str(randomnumber) + " + ")
			result += randomnumber
		print (str(self.bonus) + " = ")
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