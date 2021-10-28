from character import Character

class Enemy(Character):
    def __init__(self, name:str, alignment:str, race:str, armor_class:int, hit_points:int):
        super().__init__(name, alignment, race)
        self.__armor_class = armor_class
        self.__hit_points = hit_points
    
    def __str__(self):
        return f"This is {self.get_name()} and it is a {self.get_race()}! It has an armor class of {self.__armor_class} and {self.__hit_points} hit points!"
    
goblin = Enemy("Skullskalper", "Chaotic evil" ,"Goblin", 12, 8)

print(goblin)