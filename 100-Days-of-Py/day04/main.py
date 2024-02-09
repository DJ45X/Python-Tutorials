from termcolor import colored
import os
import random

os.system('clear')

choice = input(colored("Choose [0] for Rock, [1] for Paper or [2] Scissors:\n\n>>>", "green")).lower()
computer_choice = random.randint(0,2)

if not choice.isdigit():
    print(colored("Invalid choice! Please try again by selecting a number between 0-2", "red"))
else:
    choice = int(choice)
    if choice > 2:
        print(colored("Invalid choice! Please try again by selecting a number between 0-2", "red"))
    elif choice == 0 or choice == 1 or choice == 2:
        if choice == 0:
            print(colored("You chose Rock", "green"))
        elif choice == 1:
            print(colored("You chose Paper", "green"))
        elif choice == 2:
            print(colored("You chose Scissors", "green"))
        
        if computer_choice == 0:
            print(colored("Computer chose Rock", "green"))
            if choice == 2:
                print(colored("You lose!", "red"))
            elif choice == 0:
                print(colored("It's a tie!", "yellow"))
            else:
                print(colored("You win!", "blue"))
        
        elif computer_choice == 1:
            print(colored("Computer chose Paper", "green"))
            if choice == 0:
                print(colored("You lose!", "red"))
            elif choice == 1:
                print(colored("It's a tie!", "yellow"))
            else:
                print(colored("You win!", "blue"))
        
        elif computer_choice == 2:
            print(colored("Computer chose Scissors", "green"))
            if choice == 1:
                print(colored("You lose!", "red"))
            elif choice == 2:
                print(colored("It's a tie!", "yellow"))
            else:
                print(colored("You win!", "blue"))