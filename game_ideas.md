**If its an action, its prolly a function**
**If its an object that has other similar object, prolly a class**
**For instance, inventory doesn't need to be copied, so it shouldn't be a class...**


Class Character
    CLass Player
        Class Inventory
    Class Enemy





##TODO
- implement battle system (progress: not pretty but sufficient)
- create functions for objects
- save feature(csv file)
- inventory system (dictionary or list? nested lists?)
    -have csv with item name and price
    -make function to loop trhough and grab [name], price
    -add name loop to "add_to_in" function
- shop system
- equipping items




####Ideas
- Point system for correct or better decisions
- Random boss generator?
- Random attack points generator(dmg between x,y, random atk between x,y)
- HP
- Inventory system




####Objects
- Player
    - name
    - level
        - XP when defeating enemies
    - hp
        - below zero(is_dead = True)
        - raise hp while leveling
    - damage
        - raise dmg with weapons
    - gold
        - add when defeating enemies or finding gold
        - remove when buying items
    - Inventory (here?)
    - Equipped items/non equipped items (is_equipped = True)

- regular_monster, boss, mega_boss**special_abilities**, other_human
    - name
    - hp
    - damage

- Inventory
    - Add/Remove Items
    - Inventory Full
    - No more of item

    #####Items in Inv
        - health potion
            - half regen(.50)
            - full regen(1.0)
        -Weapons    


####General Commands
    - 'Q' = Quit
    - 'S' = Shop
    - 'I' = Inventory


####Descriptions

    General
        - Vampires(Queen Vampire Boss)
        - Ghouls
    Town
        - Vampires(Queen Vampire Boss)

    Forrest Scene (turns into swamp)
        - Wendigo
        - Manticore (Boss)
        - Medusa
    Swamp
        - Baba Yaga (Boss)

    Water Scene
        - Sirens
        - Hydra (**MEGA BOSS**)
        - Harpies
    Island
        - Land
            - Cyclops (**MEGA BOSS**)
        - Cave
            - Cave Worm




def






















|||||||FROM LEARN PYTHON THE HARD WAY |||||||||
VVVVVVV                               VVVVVVVVV


class Scene(object):
    def enter(self):
        pass


class Engine(object):
    def __init__(self, scene_map):
        pass
    def play(self):
        pass

class Death(Scene):
    def enter(self):
        pass


class Another_Scene(Scene):
    def enter(self):
        pass



class Map(object):
    def __init__(self, start_scene):
        pass
    def next_scene(self, scene_name):
        pass
    def opening_scene(self):
        pass


        examples
    a_map = Map('Another_Scene)
    a_game = Engine(a_map)
    a_game.play()    