from character import Character
from random import random



class Monk(Character):
    def __init__(self, name, race, alignment, role, creed):
        super().__init__(name, race, alignment)
        self.__class = role
        self.__creed = creed
        
    def __str__(self):
        return f"My name is {self.get_name()}. I am a {self.__class} expert in the {self.__creed}. I am a {self.get_alignment()} {self.get_race()}"

    def attack(self, weapon, damage):
        print(f"{self.get_name()} attacks with her {weapon} for {damage} points of damage!")
        attack_hit = random.randint(1, 20)
        return damage, attack_hit

sarn_vola = Monk("Sarn Vola", "Half-orc", "Chaotic Neutral", "Monk", "The way of shadows")

print(sarn_vola)
