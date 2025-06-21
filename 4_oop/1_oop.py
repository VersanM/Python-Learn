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

# Constructors
class EnemyNew:
    def __init__(self, type_of_enemy, health_points=100, attack_damage = 10):
        self.type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage
    
    def talk(self):
        print(f'I am a {self.type_of_enemy}. Be prepared to fight!')

    def walk_forward(self):
        print(f'{self.type_of_enemy} moves closer to you.')

    def attack(self):
        print(f'{self.type_of_enemy} attacks for {self.attack_damage} damage')


zombie = EnemyNew(type_of_enemy='Zombie')
zombie.talk()

# Encapsulation - use __ before private fields + add getter and setters
class EnemyEnc:
    def __init__(self, type_of_enemy, health_points=100, attack_damage = 10):
        self.__type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage

    def get_type_of_enemy(self):
        return self.__type_of_enemy
    
    def talk(self):
        print(f'I am a {self.__type_of_enemy}. Be prepared to fight!')

    def walk_forward(self):
        print(f'{self.__type_of_enemy} moves closer to you.')

    def attack(self):
        print(f'{self.__type_of_enemy} attacks for {self.attack_damage} damage')

zombie = EnemyEnc(type_of_enemy='Zombie')
zombie.talk()
print(zombie.get_type_of_enemy())