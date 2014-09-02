class BaseCharacter(object):
    def __init__(self):
        """ CHARACTER SHEET """

        # Player Name
        self.pname = ''
        # Character Name
        self.cname = ''
        # Class
        self.clazz = ''
        # Race
        self.race = 0
        # Age
        self.age = 0
        # Gender
        self.gender = ''
        # Level
        self.level = 1
        # XP
        self.xp = 0

        """ ABILITY SCORES """

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

        """ HIT POINTS """

        # Max Hit Points
        self.maxhp = 0
        # Bloodied
        self.bloodied = 0

        """ OTHERS """
        # Armor Class
        self.ac = 0
        # Gold Pieces
        self.gp = 0

    def __unicode__(self):
        return "I am " + str(self.getPname()) + ", the " + str(self.getRace())

    def __str__(self):
        return "I am " + str(self.getPname()) + ", the " + str(self.getRace())

    def set_pname(self, pname):
        self.pname = pname

    def get_pname(self):
        return self.pname

    def set_cname(self, cname):
        self.cname = cname

    def get_cname(self):
        return self.cname

    def set_clazz(self, clazz):
        self.clazz = clazz

    def get_clazz(self):
        return self.clazz

    def set_race(self, race):
        self.race = race

    def get_race(self):
        return self.race

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def set_gender(self, gender):
        self.gender = gender

    def get_gender(self):
        return self.gender

    def set_level(self, level):
        self.level = level

    def get_level(self):
        return self.level

    def set_xp(self, xp):
        self.xp = xp

    def get_xp(self):
        return self.xp

    def set_str(self, strength):
        self.str = strength

    def get_str(self):
        return self.str

    def set_con(self, con):
        self.con = con

    def get_con(self):
        return self.con

    def set_dex(self, dex):
        self.dex = dex

    def get_dex(self):
        return self.dex

    def set_int(self, intelligence):
        self.int = intelligence

    def get_int(self):
        return self.int

    def set_wis(self, wis):
        self.wis = wis

    def get_wis(self):
        return self.wis

    def set_cha(self, cha):
        self.cha = cha

    def get_cha(self):
        return self.cha

    def set_maxhp(self, maxhp):
        self.maxhp = maxhp

    def get_maxhp(self):
        return self.maxhp

    def set_bloodied(self, bloodied):
        self.bloodied = bloodied

    def get_bloodied(self):
        return self.bloodied

    def set_ac(self, ac):
        self.ac = ac

    def get_ac(self):
        return self.ac

    def set_gp(self, gp):
        self.gp = gp

    def get_gp(self):
        return self.gp
