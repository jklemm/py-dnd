
class Player(object):
	
	def __init__ (self):
		
		# object properties
		self.name = ''
		self.gender = ''

		# object attributes
		self.str = 0
		self.con = 0
		self.dex = 0
		self.int = 0
		self.wis = 0
		self.cha = 0

		# object status
		self.maxhp = 0
		self.mana = 0

	def setName(self, n):
		self.name = n

	def setGender(self, g):
		self.gender = g

