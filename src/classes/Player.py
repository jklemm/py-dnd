
class Player(object):
	
	def __init__ (self):

		''' CHARACTER SHEET '''
		
		# Player Name
		self.pname  = ''
		# Character Name
		self.cname  = ''
		# Class
		self.clazz  = 0
		# Race
		self.race   = 0
		# Age
		self.age    = 0
		# Gender
		self.gender = ''
		# Level
		self.level  = 0
		# XP
		self.xp     = 0

		''' ABILITY SCORES '''

		# Strength
		self.str = 0
		# Constituition
		self.con = 0
		# Dexterity
		self.dex = 0
		# Intelligence
		self.int = 0
		# Wisdom
		self.wis = 0
		# Charisma
		self.cha = 0

		''' HIT POINTS '''

		# Max Health Points
		self.maxhp = 0
		# Bloodied
		self.bloodied = 0

	def setName(self, n):
		self.name = n

	def setGender(self, g):
		self.gender = g

