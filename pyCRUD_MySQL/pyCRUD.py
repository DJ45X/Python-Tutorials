import options
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

options = {
    "i": options.insert,
    "s": options.search,
    "a": options.readAll,
    "u": options.update,
    "d": options.delete,
    "q": options.quit
}

while True:
    userInput_choice = input(colored("""
Select an option: 
[S]earch-By-Name, Show [A]ll, [I]nsert, [U]pdate-By-Name, [D]elete-By-Name or [Q]uit:
>>>""", "light_green"))
    
    if userInput_choice in options:
        options[userInput_choice]()
    elif userInput_choice == "q":
        quit()
    else:
        print(colored("Invalid option! Please try again!", "red"))