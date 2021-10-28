import random

class Character():
    def __init__(self, name, race, alignment):
        self.__name = name
        self.__race = race 
        self.__alignment = alignment
    
    def __str__(self):
        return f"My name is {self.__name}. I am a {self.__alignment} {self.__race}"

    def get_name(self):
        return self.__name

    def get_race(self):
        return self.__race
    
    def get_alignment(self):
        return self.__alignment

    def attack(self, weapon, damage):
        print(f"{self.get_name()} attacks with her {weapon} for {damage} points of damage!\n")
        attack_hit = random.randint(1, 20)
        return damage, attack_hit