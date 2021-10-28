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