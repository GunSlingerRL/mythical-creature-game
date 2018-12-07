
from random import randint




#Character can: buy/sell items, attack, take dmg, die, kill, level up, earn gold, equip items
class Character:
    def __init__(self, name: str, xp: int, level: int, hp: int, dmg: int, gold: int): #Inventory list or dict
        self.name = name
        self.xp = xp
        self.level = level
        self.hp = hp
        self.dmg = dmg
        self.gold = gold

    
    
    def death (self):
        if self.hp <=0:
            print(self.name + " died.")
            #return to last scene



    #returns player name
    def get_name(self):
        return self.name

    def gold_balance(self):
        return self.gold

    
    

    

    
#Enemy can: fight, die, kill
class Enemy:
    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg

    
    
    def attack(self):
        pass



class Item:

    inv = list()


    def __init__(self, name, type, desc, property):
        self.name = name
        self.type = type
        self.desc = desc
        self.property = property


    def add_item(self,item):
        self.item = item
        Item.inv.append(item)
        return Item.inv
        

    def drop_item(self, item):
        self.item = item
        Item.inv.remove(item)
        return Item.inv


