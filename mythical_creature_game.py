#Help, contributions and guidance by Bareknuckles


import os
from page_objects import PageObject
import pages
from test_classes import Player


# clears the screen for windows or linux/uni
def clearScreen():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")


username = input("please enter name >")

player = Player(username, 1, 100, 25, 0)

#function to inititate game
def main():
    # dictionary containing all our page objects stored by their PAGE_INDEX
    # pageDict = dict()
    pageDict: dict = pages.getPages()

   

    playing: bool = True  # we play till we aren't
    currentPage: str = "START"  # have to start somewhere, why not the "start" =P

    while playing:  # we play till we aren'tb

        clearScreen()
        thisPage: PageObject = pageDict.get(currentPage)
        print(thisPage.scene)
        # thisPage.get_scene()
    
    #####if thisPage.scene == "blah":
                #encounter(enemy)
                #if enemy.hp <= 0:
                    #print("enemy defeated")
                    #print(thisPage.scene) <<<<<<<Whatever next scene would've been before encounter
                #elif player.hp <= 0:
                    #print you died
                    #print(thisPage.scene) <<<<<Where the .scene == "death"

       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # Get user input as uppercase to make things easy on usb

        userInput: str = input("> ").upper()

        # test user input against special hard commands like 'quit' before comaring to the pages commands
        if userInput == "Q":
            playing = False
        elif userInput in thisPage.commands:
            currentPage = thisPage.commands.get(userInput)

    print("\r\nGoodbye!\r\n")

if __name__ == "__main__":
    main()
