# Polymorphism 

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

    def attack(self):
        print(f"{self.__type_of_enemy} attacks for {self.attack_damage} damage")

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
    

def battle(e: Enemy):
    e.talk()
    e.attack()

zombie = Zombie(10, 1)
ogre = Ogre(20, 3)

battle(zombie)
battle(ogre)
