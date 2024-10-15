#  print colors on python console
from Basics.colours import YELLOW_BG

import colorama
RESET = "\033[0m"
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# format the background
BLACK = "\033[40m"
RED_BG = "\033[41m"
GREEN_BG = "\033[42m"
YELLOW_BG = "\033[43m"
BLUE_BG = "\033[44m"
MAGENTA_BG = "\033[45m"
CYAN_BG = "\033[46m"
WHITE_BG = "\033[47m"

#Get input from user for the following
print(BLUE + "Hi, Welcome to the world of programming, hope you will enjoy this simple questionaire")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your current age: "))
address = input("Enter your full address: ")

if age>35<45:

    print(BLACK + WHITE_BG + f"Your name is {first_name.upper()} {last_name.upper()}. You are {age} this year and you are residing at {address.upper()}")
    print(GREEN + YELLOW_BG + "Continue to rest at home")
else    age>=45<55:
    print (MAGENTA + YELLOW_BG + "Get Ready to claim your CPF. Not too much but at least something")
if age>55<75:
    print("Time to retire")
else:    
    print(RED + YELLOW_BG + "Continue working all the way")


  #print(f"Your current working status is {working_status}")


