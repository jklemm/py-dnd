
from classes.CommandLineInterface import *
from classes.Player import *

class Game(object):
	
	def __init__ (self):
		self.player = Player()
	
	def logo(self):
		print ("                                                                          ")
		print ("                                             88                        88 ")
		print ("                                             88                        88 ")
		print ("                                             88                        88 ")
		print ("8b,dPPYba,   8b       d8             ,adPPYb,88  8b,dPPYba,    ,adPPYb,88 ")
		print ("88P'    \"8a  `8b     d8'  aaaaaaaa  a8\"    `Y88  88P'   `\"8a  a8\"    `Y88 ")
		print ("88       d8   `8b   d8'   \"\"\"\"\"\"\"\"  8b       88  88       88  8b       88 ")
		print ("88b,   ,a8\"    `8b,d8'              \"8a,   ,d88  88       88  \"8a,   ,d88 ")
		print ("88`YbbdP\"'       Y88'                `\"8bbdP\"Y8  88       88   `\"8bbdP\"Y8 ")
		print ("88               d8'                                                      ")
		print ("88              d8'                                                       ")
		print ("                                                                          ")

	def mainMenu(self):
		print ("MENU")
		print ("------")
		print ("1-New Game")
		print ("2-Load Game")
		print ("3-Credits")
		print ("4-Exit")

	def start(self):
		self.logo()
		
		self.mainMenu()

		name = input("Player name:")
		self.player.setName(name)

		gender = input("Player gender:")
		self.player.setGender(gender)

		pause()