from commandlineinterface import *
from character import *


class Game(object):
    def __init__(self):
        self.player = BaseCharacter()

    def logo(self):
        print "                                                                          "
        print "                                             88                        88 "
        print "                                             88                        88 "
        print "                                             88                        88 "
        print "8b,dPPYba,   8b       d8             ,adPPYb,88  8b,dPPYba,    ,adPPYb,88 "
        print "88P'    \"8a  `8b     d8'  aaaaaaaa  a8\"    `Y88  88P'   `\"8a  a8\"    `Y88 "
        print "88       d8   `8b   d8'   \"\"\"\"\"\"\"\"  8b       88  88       88  8b       88 "
        print "88b,   ,a8\"    `8b,d8'              \"8a,   ,d88  88       88  \"8a,   ,d88 "
        print "88`YbbdP\"'       Y88'                `\"8bbdP\"Y8  88       88   `\"8bbdP\"Y8 "
        print "88               d8'                                                      "
        print "88              d8'                                                       "
        print "                                                                          "

    def main_menu(self):
        print "MENU"
        print "-----------"
        print "1-New Game"
        print "2-Load Game"
        print "3-Credits"
        print "4-Exit"
        print "-----------"

        option = input_number("Press a number and hit Enter: ", 1, 4)

        if option == 1:
            self.new_game()
        elif option == 2:
            self.load_game()
        elif option == 3:
            self.credits()
        elif option == 4:
            exit()

    def new_game(self):
        clear()
        print "-----------"
        print "NEW GAME"
        print "-----------"
        print "Welcome to the world of Dungeons and Dragons!"

        name = input_string("First, select your Player's name and press Enter: ")

        player = BaseCharacter()
        player.set_pname(name)

        print "Ok " + name + "!"

        race = input_string("Now select your Player's Race and press Enter: ")
        player.set_race(race)

        print str(player)

    def load_game(self):
        pass

    def credits(self):
        pass

    def start(self):
        """
        The initial method of game
        """
        self.logo()
        while True:
            self.main_menu()
            pause()