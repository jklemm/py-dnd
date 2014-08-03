
import os

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

def pause():
	os.system('pause')

def userInputNumber(message, minimum, maximum):
	userInput = 0
	while True:
		try:
			userInput = int(input(message))
			if (userInput < minimum or userInput > maximum):
				raise IndexError("The input integer is out of the allowed range!")
		except ValueError:
			print ("The input value is not an valid integer!")
			continue
		except IndexError as error:
			print (str(error))
			continue
		else:
			break
	return userInput
