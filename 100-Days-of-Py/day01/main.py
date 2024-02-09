from termcolor import colored

print(colored("Welcome to the Team Name Generator!", "green"))

city = input(colored("What's the name of the city you grew up in?\n", "light_blue"))
pet = input(colored("What's your pet's name?\n", "light_blue"))

print(colored(f"Your team name could be {city} {pet}", "yellow"))