from monk import Monk
from enemy import Enemy

class Game():
    '''Game '''
    def __init__(self, character, enemy:Enemy):
        self.__character = character
        self.__enemy = enemy

    def __str__(self) -> str:
        return f"{self.__character.get_name()} is fighting {self.__enemy.get_name()}!"
        
    def start(self):
        damage, attack_hit = self.__character.attack("Mace", 4)

        print(f"{self.__enemy.get_name()} has an armor class of {self.__enemy.get_ac()}")

        if(attack_hit >= self.__enemy.get_ac()):
            self.__enemy.take_damage(damage)
            print(f"{self.__enemy.get_name()} takes {damage} points of damage! It has {self.__enemy.get_hit_points()} hit points left!")
            
        else:
            print("The attack missed!")

character = Monk("Sarn Vola", "Half-orc", "Chaotic Neutral", "Monk", "The way of shadows")
enemy = Enemy("Skullskalper", "Chaotic evil" ,"Goblin", 12, 8)

game = Game(character, enemy)
print(game)
print("\n")
game.start()

