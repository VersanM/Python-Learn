# Constructors
class Enemy:
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


zombie = Enemy(type_of_enemy='Zombie')
zombie.talk()