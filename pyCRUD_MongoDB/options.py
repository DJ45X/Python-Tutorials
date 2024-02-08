import utils
from termcolor import colored

def insert():
    name = input(colored("Enter your name:  ", "light_yellow"))
    address = input(colored("Enter your address:  ", "light_yellow"))
    utils.create(name, address)

def search():
    name = input(colored("Enter a name you wish to search for:  ", "light_yellow"))
    utils.searchByName(name)

def readAll():
    utils.readAll()

def update():
    oldName = input(colored("Enter the name of the record to be updated:  ", "light_yellow"))
    newName = input(colored("Provide a new name:  ", "light_yellow"))
    newAddress = input(colored("Provide a new address:  ", "light_yellow"))
    utils.update(oldName, newName, newAddress)

def delete():
    name = input(colored("Enter the name of the record to be deleted:  ", "light_yellow"))
    utils.delete(name)

def quit():
    print(colored("Goodbye!", "light_red"))
    exit()