import os
from page_objects import PageObject
import pages
from test_classes import Player, Enemy
from test_classes import *

def clearScreen():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")


player = Player("kyle", 1, 100, 25, 50)
manticore = Enemy("manticore", 300, 10)
potion = Item("health potion", 12, 20)

# playing = True
# while playing:
#         manticore.hp -= player.dmg
#         print("enemy hp: " + str(manticore.hp))
#         print()
#         player.hp -= manticore.dmg
#         print("your health: " + str(player.hp))
#         print()

#         if manticore.hp <=0:
#                 print("manticore dead")
#                 playing = False
#         if player.hp <=0:
#                 print("you dead")
#                 playing = False


#         user_input = input("buy/sell")

#         if user_input == "buy":
#                  player.gold -= 10
#                  print(player.gold)
#         elif user_input == "sell":
#                 player.gold += 10 
#                 print(player.gold)


                # revive to full health but not past player default hp
        # userInput = input("use revive?")

        # if userInput == "y":
        #         player.hp = 200
        #         print(player.hp)
        #         if player.hp > 100:
        #                 player.hp =100
        #                 print(player.hp)

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

        # Get user input as uppercase to make things easy on usb

        userInput: str = input("> ").upper()

        if userInput == "a":
               print("You attack the ghoul")
       
       
       
       
       
       
       
       
       
       
       
        # test user input against special hard commands like 'quit' before comaring to the pages commands
        if userInput == "Q":
            playing = False
        elif userInput in thisPage.commands:
            currentPage = thisPage.commands.get(userInput)

    print("\r\nGoodbye!\r\n")

if __name__ == "__main__":
    main()

        
        

