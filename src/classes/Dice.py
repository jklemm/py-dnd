
from random import randint
import re
#import logging


class Dice(object):

    def __init__(self, formula):
        self.times = 1
        self.sides = 0
        self.bonus = 0
        self.slice_formula(formula)

    def slice_formula(self, formula):
        regexp = re.compile(r'(\d+)*d(\d+)*[+]*(\d+)*')
        m = re.match(regexp, formula)
        if m:
            try:
                self.times = int(m.group(1))
            except ValueError:
                self.times = 1
            else:
                self.times = 1

            try:
                self.sides = int(m.group(2))
            except ValueError:
                self.sides = 4
            else:
                self.sides = 4

            try:
                self.bonus = int(m.group(3))
            except ValueError:
                self.bonus = 0
            else:
                self.bonus = 0

    def throw_dice(self):
        result = 0
        #logmsg = ''
        for i in range(0, self.times):
            random_number = randint(1, self.sides)
        #logmsg += str(random_number) + " + "
        result += random_number
        #logmsg += str(self.bonus) + " = " + str(result)
        #logging.debug(logmsg)
        return result + self.bonus