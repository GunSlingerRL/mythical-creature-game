#Help, contributions and guidance by Bareknuckles

import os
import random
from page_objects import PageObject
import pages
from test_classes import Character, Enemy
from instances import vampire, norm_enemy, boss, mega_boss, final_boss

# clears the screen for windows or linux/uni
def clearScreen():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")

#username = input("please enter name >")

player = Character("username", 0, 1, 100, 25, 0)




player.add_to_inv("sword", 1)

print(player.inventory)









#function to inititate game
#def main():


   

        # while playing == True:
       
            

                            #BATTLE PHASE   
#=========================Set this as a class function, but replace vampire with enemy argument?
            # while player.hp> 0 or vampire.hp > 0:
                
                
            #     #Player attack phase
            #     player_hit = random.randint((player.dmg - 10), player.dmg)
            #     rand_enemy.hp -= player_hit
            #     print("you hit " + rand_enemy.name + " for: " + str(player_hit))
            #     if player_hit > player.dmg - 5:
            #         print("CRITICAL HIT!")
            #     if rand_enemy.hp <= 0:
            #         print(rand_enemy.name + " didn't stand a damn chance!")
            #         print()
            #         print("you gained: " + str(player.gold) + " gold")
            #         playing = False
            #         break

            #     #Enemy attack phase
            #     enemy_hit = random.randint(0, rand_enemy.dmg)
            #     player.hp -= enemy_hit
            #     if enemy_hit == 0:
            #         print("vampire missed")
            #     else:
            #         print(rand_enemy.name +" hit you for: " + str(enemy_hit))
            #     if player.hp <= 0:
            #         print(player.death)
            #         playing = False
            #         break
#===========================End Battle Phase============================================

                
                
                
        



#if __name__ == "__main__":
#    main()
