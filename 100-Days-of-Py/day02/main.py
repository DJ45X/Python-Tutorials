import os
from termcolor import colored

# Clear the terminal
os.system("clear")

print(colored("DJ's Tip Calculator\n\n", "green"))

bill = float(input(colored("What was the total bill?\n$ ", "blue")))
tip = int(input(colored("What percentage tip would you like to give?\n8%, 10%, 12%, or 15%? ", "blue")))
split = int(input(colored("How many in your party to split the bill?\nPeople: ", "blue")))

total = ("{:.2f}".format((((bill * (tip / 100)) + bill) / split)))

print(colored(f"Each person should pay: ${total}", "green"))