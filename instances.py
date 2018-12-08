#creating instances here from test_classes so I won't have a huge instance list on main
from test_classes import Item, Character, Enemy





#Creating some items
potion = Item("HP Potion", "potion", "Heals for 50 points", 50 )
max_potion = Item("Max Heal", "potion", "Heals for full HP", 9999)



#Creating Enemies

#Regular enemies
vampire = Enemy("Vampire",75, 10)
ghoul = Enemy("Ghoul", 50, 5)
harpy = Enemy("Harpy", 50, 10)
siren = Enemy("Siren", 75, 20)
cave_worm = Enemy("Cave Worm", 150, 10)



#Bosses
vampire_queen = Enemy("Vampire Queen", 150, 25)
hydra = Enemy("Hydra", 250, 40)
cyclops = Enemy("Cyclops", 275, 35)
baba_yaga = Enemy("Baba Yaga", 125, 25)

#Mega Bosses
sister_fate_one = Enemy("First sister of the Fate", 400, 50)
sister_fate_two = Enemy("Second sister of the Fate", 300, 75)
sister_fate_three = Enemy("Last sister of the Fate", 500, 75) 

grim_reaper= Enemy("Angel of Death", 800, 90)


norm_enemy = [vampire, ghoul, harpy, siren, cave_worm]
boss = [vampire_queen, hydra, cyclops, baba_yaga]
mega_boss = [sister_fate_one, sister_fate_two, sister_fate_three]
final_boss = [grim_reaper]