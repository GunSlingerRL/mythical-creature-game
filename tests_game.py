import os
from page_objects import PageObject
import pages
from test_classes import Player, Enemy



player = Player("kyle", 1, 100, 25, 50)
manticore = Enemy("manticore", 300, 10)
potion = Item("health potion", 12, 20)

playing = True
while playing:
        manticore.hp -= player.dmg
        print("enemy hp: " + str(manticore.hp))
        print()
        player.hp -= manticore.dmg
        print("your health: " + str(player.hp))
        print()

        if manticore.hp <=0:
                print("manticore dead")
                playing = False
        if player.hp <=0:
                print("you dead")
                playing = False


        user_input = input("buy/sell")

        if user_input == "buy":
                 player.gold -= 10
                 print(player.gold)
        elif user_input == "sell":
                player.gold += 10 
                print(player.gold)


                # revive to full health but not past player default hp
        # userInput = input("use revive?")

        # if userInput == "y":
        #         player.hp = 200
        #         print(player.hp)
        #         if player.hp > 100:
        #                 player.hp =100
        #                 print(player.hp)


        
        

