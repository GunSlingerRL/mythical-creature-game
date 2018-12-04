class Player:
    def __init__(self, name: str, level: int, hp: int, dmg: int, gold: int): #Inventory list or dict
        self.name = name
        self.level = level
        self.hp = hp
        self.dmg = dmg
        self.gold = gold
    
    
    
    
class Enemy:
    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg



class Inventory:

    inv = list()


    def __init__(self, item_name):
        pass


    def add_item(self,item):
        self.item = item
        
        

    def drop_item(self, item):
        self.item = item 
        