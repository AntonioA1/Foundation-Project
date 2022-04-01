
def validate_int(usr_input):
    try:
        return int(usr_input)
    except:
        return -1

def shirt():  
    while True:
        try:
            val = int(input("\tWhich shirt was sold: 1. Blue, 2. Red, or 3. Black? "))
            if (val > 0) and (val <= 3):
                return val
            else:
                print("Invalid Input, please enter a correct input.")
        except:
            print("Input must be a integer, please try again")
    
def get_units():
    while True:
        try:
            val = int(input("\n Please enter number of units: "))
            if (val > 0):
                return val
            else:
                print("Invalid Input, please enter a correct input.")
        except:
            print("Input must be a integer, please try again")