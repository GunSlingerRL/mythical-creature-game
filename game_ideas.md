##TODO
- implement battle system
-create functions for objects





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






####Verbs
- Attack
- Taking damage
- Healing
- Moving?


####Rooms
- Tavern
- Forrest
- Sea
- Swamp
- Island
- Cave

####General Commands
    - 'Q' = Quit
    - 'S' = Shop
    - 'I' = Inventory

####Synopsis





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







