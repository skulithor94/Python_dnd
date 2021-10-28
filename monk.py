import sys
sys.path.append('../')

from character import Character

class Monk(Character):
    def __init__(self, name, race, alignment, role, creed):
        super().__init__(name, race, alignment)
        self.__class = role
        self.__creed = creed
        
    def __str__(self):
        return f"My name is {self.get_name()}. I am a {self.__class} expert in the {self.__creed}. I am a {self.get_alignment()} {self.get_race()}\n"

sarn_vola = Monk("Sarn Vola", "Half-orc", "Chaotic Neutral", "Monk", "The way of shadows")

print(sarn_vola)
