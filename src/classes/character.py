
class BaseCharacter(object):
	
	def __init__ (self):

		''' CHARACTER SHEET '''
		
		# Player Name
		self.pname  = ''
		# Character Name
		self.cname  = ''
		# Class
		self.clazz  = ''
		# Race
		self.race   = 0
		# Age
		self.age    = 0
		# Gender
		self.gender = ''
		# Level
		self.level  = 1
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

		# Max Hit Points
		self.maxhp = 0
		# Bloodied
		self.bloodied = 0

		''' OTHERS '''
		# Armor Class
		self.ac = 0
		# Gold Pieces
		self.gp = 0

	def __unicode__(self):
		return "I am "+str(self.getPname())+", the "+str(self.getRace())

	def __str__(self):
		return "I am "+str(self.getPname())+", the "+str(self.getRace())

	def setPname(self, pname):
		self.pname = pname

	def getPname(self):
		return self.pname

	def setCname(self, cname):
		self.cname = cname

	def getCname(self):
		return self.cname

	def setClazz(self, clazz):
		self.clazz = clazz

	def getClazz(self):
		return self.clazz

	def setRace(self, race):
		self.race = race

	def getRace(self):
		return self.race

	def setAge(self, age):
		self.age = age

	def getAge(self):
		return self.age

	def setGender(self, gender):
		self.gender = gender

	def getGender(self):
		return self.gender

	def setLevel(self, level):
		self.level = level

	def getLevel(self):
		return self.level

	def setXp(self, xp):
		self.xp = xp

	def getXp(self):
		return self.xp

	def setStr(self, strength):
		self.str = strength

	def getStr(self):
		return self.str

	def setCon(self, con):
		self.con = con

	def getCon(self):
		return self.con

	def setDex(self, dex):
		self.dex = dex

	def getDex(self):
		return self.dex

	def setInt(self, int):
		self.int = int

	def getInt(self):
		return self.int

	def setWis(self, wis):
		self.wis = wis

	def getWis(self):
		return self.wis

	def setCha(self, cha):
		self.cha = cha

	def getCha(self):
		return self.cha

	def setMaxhp(self, maxhp):
		self.maxhp = maxhp

	def getMaxhp(self):
		return self.maxhp

	def setBloodied(self, bloodied):
		self.bloodied = bloodied

	def getBloodied(self):
		return self.bloodied

	def setAc(self, ac):
		self.ac = ac

	def getAc(self):
		return self.ac

	def setGp(self, gp):
		self.gp = gp

	def getGp(self):
		return self.gp





