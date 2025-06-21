# Inheritance
class Animal:
    weight: int
    color: str
    age: int
    animal_type: str

    def eat(self):
        print("Animal eating")
    
    def sleep(self):
        print("Animal sleeping")

class Dog(Animal):
    # all animal attributes
    can_shed: bool
    domestic_name: str

    def talk(self):
        print("Bark!")

    def eat(self):
        print("Chews on bone!")

class Enemy:
    def __init__(self, type_of_enemy, health_points, attack_damage):
        self.__type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage

    def get_type_of_enemy(self):
        return self.__type_of_enemy
    
    def talk(self):
        print("I am an Enemy!")

    def walk_forward(self):
        print(f"{self.__type_of_enemy} moves closer to you")

class Zombie(Enemy):
    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy='Zombie', health_points=health_points, attack_damage=attack_damage)

    def talk(self):
        print('*Grumbling...*')

    def spread_disease(self):
        print('The zombie is trying to spread infection')

class Ogre(Enemy):
    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy='Ogre', health_points=health_points, attack_damage=attack_damage)

    def talk(self):
        print('Ogre is slamming hands all around.')
    
zombie = Zombie(10, 1)
print(zombie.get_type_of_enemy())
print(zombie.talk())
print(zombie.walk_forward())
print(zombie.spread_disease())

ogre = Ogre(20, 3)
print(ogre.get_type_of_enemy())
print(ogre.talk())
print(ogre.walk_forward())