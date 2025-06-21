# class declaration
class Enemy:
    type_of_enemy: str
    health_points: int = 100
    attack_damage: int = 10

    def talk(self):
        print(f'I am a {self.type_of_enemy}. Be prepared to fight!')

    def walk_forward(self):
        print(f'{self.type_of_enemy} moves closer to you.')

    def attack(self):
        print(f'{self.type_of_enemy} attacks for {self.attack_damage} damage')


zombie = Enemy()
zombie.type_of_enemy = 'Zombie'
print(f'{zombie.type_of_enemy} has {zombie.health_points} health points and can do an attack damage of {zombie.attack_damage}')

# Abstraction
print(zombie.talk())

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

class EnemyBase:
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

