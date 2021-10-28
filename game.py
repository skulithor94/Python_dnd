from monk import Monk
from enemy import Enemy

class Game():
    def __init__(self, monk:Monk, enemy:Enemy):
        self.__character = monk
        self.__enemy = enemy

    def __str__(self) -> str:
        return f"{self.__character.get_name()} is fighting {self.__enemy.get_name()}!"
        
monk = Monk("Sarn Vola", "Half-orc", "Chaotic Neutral", "Monk", "The way of shadows")
enemy = Enemy("Skullskalper", "Chaotic evil" ,"Goblin", 12, 8)

game = Game(monk, enemy)

print(game)