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

    def attacked(self, dmg):
        self.dmg = dmg
        
    


class Item:

    inv = list()


    def __init__(self, name, sell_price, buy_price):
        self.name = name
        self.sell_price = sell_price
        self.buy_price = buy_price


    def add_item(self,item):
        self.item = item
        Item.inv.append(item)
        return Item.inv
        

    def drop_item(self, item):
        self.item = item
        Item.inv.remove(item)
        return Item.inv