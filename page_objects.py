class PageObject:
    def __init__(self, scene: str, commands: dict):
        self.scene = scene
        self.commands = commands

    def change_desc(self, descript: str):
        self.scene = descript

    # add single command to dictionary
    def add_cmd(self, command: str , index: str):
        self.commands[command] = index
    
    # add multiple commands at one time using dictionary format
    # {"KEY": "INDEX_VALUE"}
    def add_cmds(self, cmdDict: dict):
        self.commands.update(cmdDict)




#--------------------------------CREATURES AND PLAYER

class Player:
    def __init__(self, name: str, level: int, hp: int, dmg: int, gold: int, inventory): #Inventory list or dict
        self.name = name
        self.level = level
        self.hp = hp
        self.dmg = dmg
        self.gold = gold
    
    def add_remove_inv(self):
        pass
    
class Enemies:
    def __init__(self, name, hp, dmg):
        pass

    def boss(self):
        pass

    def mega_boss(self):
        pass    
