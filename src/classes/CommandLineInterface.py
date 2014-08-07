
import os

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

def pause():
	if os.name == 'nt':
		os.system('pause')
	else:
		raw_input("\nPress any key to continue...\n")
		clear()

def userInputNumber(message, minimum, maximum):
	userInput = 0
	while True:
		try:
			userInput = int(raw_input(message))
			if (userInput < minimum or userInput > maximum):
				raise IndexError("The input integer is out of the allowed range!")
		except ValueError:
			print "The input value is not an valid integer!"
			continue
		except IndexError as error:
			print str(error)
			continue
		else:
			break
	return userInput

def userInputString(message):
	userInput = ''
	while True:
		try:
			userInput = raw_input(message)
		except ValueError:
			print "The input value is not an valid text!"
			continue
		else:
			break
	return userInput
