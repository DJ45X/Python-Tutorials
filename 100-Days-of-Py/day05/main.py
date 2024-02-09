import random
from termcolor import colored
import os

os.system('clear')

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print(colored("Welcome to the pyPassword Generator!", "blue"))
nr_letters = input(colored("How many letters would you like in your password?\n", "green"))
nr_symbols = input(colored("How many symbols would you like?\n", "green"))
nr_numbers = input(colored("How many numbers would you like?\n", "green"))

if not nr_letters.isdigit() or not nr_symbols.isdigit() or not nr_numbers.isdigit():
    print(colored("Invalid input! Please try again.", "red"))
else:
    password = []

    random_letter = random.randint(0, 51)
    for i in range(0, int(nr_letters)):
        password.append(letters[random_letter])

    random_number = random.randint(0, 9)
    for i in range(0, int(nr_numbers)):
        password.append(numbers[random_number])

    random_symbol = random.randint(0, 8)
    for i in range(0, int(nr_symbols)):
        password.append(symbols[random_symbol])

    random.shuffle(password)
    print(colored(f"Your generated password is: {''.join(password)}"))

    if len(password) <= 6:
        print(colored("Your password is weak! Please try again with at least 8 characters for a stronger password.", "red"))
    elif len(password) <= 10:
        print(colored("Your password is moderate. Please try again with at least 8 characters for a stronger password.", "yellow"))
    else:
        print(colored("Your password is strong!", "green"))