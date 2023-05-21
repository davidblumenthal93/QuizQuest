class Character():
    def __init__(self):
        self.character_class = ""
        self.health = 0
        self.attack = 0
        self.defense = 0
        self.art = ""

    def take_damage(self, damage):
        self.health -= damage
        print (f"{self.character_class} has taken 10 damage.")

    @staticmethod
    def select_class(self):
        class_choice = input("Please select a Class: 1.Warrior, 2.Mage, 3.Ranger")
        if class_choice == "1":
            Warrior()
        elif class_choice == "2":
            Mage()
        elif class_choice == "3":
            Ranger()
 

class Warrior(Character):
    def __init__(self):
        self.character_class = "Warrior"
        self.health = 100
        self.attack = 10
        self.defense = 10
        self.art = ""
        self.damage = 10

    def take_damage(self, damage):
        super().take_damage(damage)

class Mage(Character):
    def __init__(self):
        self.character_class = "Mage"
        self.health = 100
        self.attack = 10
        self.defense = 10
        self.art = ""

    def take_damage(self, damage):
        super().take_damage(damage)

class Ranger(Character):
    def __init__(self):
        self.character_class = "Ranger"
        self.health = 100
        self.attack = 10
        self.defense = 10
        self.art = ""

    def take_damage(self, damage):
        super().take_damage(damage)




# Elf

# Orc

# Wizard