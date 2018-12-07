#Help, contributions and guidance by Bareknuckles


import os
from page_objects import PageObject
import pages
from test_classes import Character, Enemy
import instances

# clears the screen for windows or linux/uni
def clearScreen():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")

#username = input("please enter name >")

player = Character("username", 0, 1, 100, 25, 0)


# def encounter():
        
#         while ghoul.hp > 0 or player.hp > 0:
#             print("You attack!")
#             ghoul.hp -= player.dmg
            
#             print("You did " + str(player.dmg) + " damage.")
#             print(ghoul.hp)
#             print("Ghoul attacks!")
#             player.hp -= ghoul.dmg
#             print("Ghoul did " + str(ghoul.dmg) + " damage.")
#             print(player.hp)
#             if player.hp <= 0:
#                 print("you are dead")
#                 #send to die function
#             elif ghoul.hp <= 0:
#                 print("ghoul is dead")
                
           
        



#function to inititate game
def main():


    #encounter()
    player.hp = 1
    player.death()
    print(player.hp)
    player.hp = -4
    player.death()
    print(player.hp)
    # dictionary containing all our page objects stored by their PAGE_INDEX
    # pageDict = dict()
    #pageDict: dict = pages.getPages()

   

    #playing: bool = True  # we play till we aren't
    #currentPage: str = "START"  # have to start somewhere, why not the "start" =P

    # while playing:  # we play till we aren'tb

    #     clearScreen()
    #     thisPage: PageObject = pageDict.get(currentPage)
    #     print(thisPage.scene)
    #     # thisPage.get_scene()
    


    



            #print(thisPage.scene) <<<<<Where the .scene == "death"


    #####if thisPage.scene == "blah":
                #encounter(enemy)
                #if enemy.hp <= 0:
                    #print("enemy defeated")
                    #print(thisPage.scene) <<<<<<<Whatever next scene would've been before encounter
                #elif player.hp <= 0:
                    #print you died
                    #print(thisPage.scene) <<<<<Where the .scene == "death"

       
       
       
       
       
    
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # Get user input as uppercase to make things easy on usb

        #userInput: str = input("> ").upper()

        # test user input against special hard commands like 'quit' before comaring to the pages commands
        #if userInput == "Q":
            #playing = False
        #elif userInput in thisPage.commands:
           ##print("\r\nGoodbye!\r\n")

if __name__ == "__main__":
    main()
