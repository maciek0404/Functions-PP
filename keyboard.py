###
# Functions to read any data type from the keyboard
#

def input_string(message):
    string = str(input(message))
    return string


def input_integer(message):
    while True:
        try:
            integer = int(input(message))
            return integer
        except ValueError:
            print("Error: enter a valid integer!")


def input_real(message):
    while True:
        try:
            real = float(input(message))
            return real
        except ValueError:
            print("Error: enter a valid real number!")


def input_boolean(message):
    while True:
        boolean = input(message).lower()
        if boolean == 'y':
            return True
        elif boolean == 'n':
            return False
        else:
            print("Press 'y' for yes or 'n' for no.")