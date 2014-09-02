import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def pause():
    if os.name == 'nt':
        os.system('pause')
    else:
        raw_input("\nPress any key to continue...\n")
        clear()


def input_number(message, minimum, maximum):
    user_input = 0
    while True:
        try:
            user_input = int(raw_input(message))
            if user_input < minimum or user_input > maximum:
                raise IndexError("The input integer is out of the allowed range!")
        except ValueError:
            print "The input value is not an valid integer!"
            continue
        except IndexError as error:
            print str(error)
            continue
        else:
            break
    return user_input


def input_string(message):
    user_input = ''
    while True:
        try:
            user_input = raw_input(message)
        except ValueError:
            print "The input value is not an valid text!"
            continue
        else:
            break
    return user_input
