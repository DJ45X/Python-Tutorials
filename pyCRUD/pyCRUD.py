# from insertFunction import insertInto
# from searchByName import selectFrom
# from showAll import selectAll
# from updateFunction import updateFor
# from deleteFunction import deleteBy
import dbUtils
import os
from termcolor import colored

os.system("clear")

pictoArt = """
 _____       __     ______        ______   __     ______     ______     ______                 
/\  __-.    /\ \   /\  ___\      /\  ___\ /\ \   /\  == \   /\  ___\   /\__  _\                
\ \ \/\ \  _\_\ \  \ \___  \     \ \  __\ \ \ \  \ \  __<   \ \___  \  \/_/\ \/                
 \ \____- /\_____\  \/\_____\     \ \_\    \ \_\  \ \_\ \_\  \/\_____\    \ \_\                
  \/____/ \/_____/   \/_____/      \/_/     \/_/   \/_/ /_/   \/_____/     \/_/                
                                                                                               
 ______   __  __     ______   __  __     ______     __   __        ______     ______   ______  
/\  == \ /\ \_\ \   /\__  _\ /\ \_\ \   /\  __ \   /\ "-.\ \      /\  __ \   /\  == \ /\  == \ 
\ \  _-/ \ \____ \  \/_/\ \/ \ \  __ \  \ \ \/\ \  \ \ \-.  \     \ \  __ \  \ \  _-/ \ \  _-/ 
 \ \_\    \/\_____\    \ \_\  \ \_\ \_\  \ \_____\  \ \_\\"\_\     \ \_\ \_\  \ \_\    \ \_\   
  \/_/     \/_____/     \/_/   \/_/\/_/   \/_____/   \/_/ \/_/      \/_/\/_/   \/_/     \/_/   
                                                                                               
                An application to perform CRUD operations on a MySQL database.
                                        Made by DJ45X.
  """
print(colored(pictoArt, "blue"))

while True:
    userInput_choice = input(colored("""
Select an option: 
[S]earch-By-Name, Show [A]ll, [I]nsert, [U]pdate-By-Name, [D]elete-By-Name or [Q]uit:
""", "light_green"))

    if userInput_choice == "s":
        name = input(colored("Enter a name you wish to search for:  ", "light_yellow"))
        dbUtils.searchByName(name)

    elif userInput_choice == "i":
        name = input(colored("Enter your name:  ", "light_yellow"))
        address = input(colored("Enter your address:  ", "light_yellow"))
        dbUtils.create(name, address)

    elif userInput_choice == "a":
        dbUtils.readAll()     

    elif userInput_choice == "u":
        oldName = input(colored("Enter the name of the record to be updated:  ", "light_yellow"))
        newName = input(colored("Provide a new name:  ", "light_yellow"))
        newAddress = input(colored("Provide a new address:  ", "light_yellow"))
        dbUtils.update(oldName, newName, newAddress)

    elif userInput_choice == "d":
        name = input(colored("Enter the name of the record to be deleted:  ", "light_yellow"))
        dbUtils.delete(name)

    elif userInput_choice == "q":
        print(colored("Goodbye!", "light_red"))
        break

    else:
        print(colored("Invalid input!", "red"))
