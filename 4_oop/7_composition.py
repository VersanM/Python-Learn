# Composition - HAS A relationship

import random

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

    def special_attack(self):
        print("Enemy has no special attack.")

class Zombie(Enemy):
    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy='Zombie', health_points=health_points, attack_damage=attack_damage)

    def talk(self):
        print('*Grumbling...*')

    def spread_disease(self):
        print('The zombie is trying to spread infection')

    def special_attack(self):
        did_special_attack_work = random.random() < 0.5
        if did_special_attack_work:
            self.health_points += 2
            print('Zombie regenerated 2HP!')

class Ogre(Enemy):
    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy='Ogre', health_points=health_points, attack_damage=attack_damage)

    def talk(self):
        print('Ogre is slamming hands all around.')

    def special_attack(self):
        did_special_attack_work = random.random() < 0.2
        if did_special_attack_work:
            self.attack_damage += 4
            print('Ogre gets angry and increases attack by 4!')

class Weapon:
    def __init__(self, weapon_type, attack_increase):
        self.weapon_type = weapon_type
        self.attack_increase = attack_increase

class Hero:
    def __init__(self, health_points, attack_damage):
        self.health_points = health_points
        self.attack_damage = attack_damage
        self.is_weapon_equipped = False
        self.weapon: Weapon = None
    
    def equip_weapon(self):
        if self.weapon is not None and not self.is_weapon_equipped:
            self.attack_damage += self.weapon.attack_increase
            self.is_weapon_equipped = True

    def attack(self):
        print(f'Hero attacks for {self.attack_damage} damage.')
        

def battle(e1: Enemy, e2: Enemy):
    e1.talk()
    e2.talk()

    while e1.health_points > 0 and e2.health_points > 0:
        print('------------')
        e1.special_attack()
        e2.special_attack()
        print(f'{e1.get_type_of_enemy()}: {e1.health_points} HP left')
        print(f'{e2.get_type_of_enemy()}: {e2.health_points} HP left')
        e2.attack()
        e1.health_points -= e2.attack_damage
        e1.attack()
        e2.health_points -= e1.attack_damage

    print('------------')
    if e1.health_points > 0:
        print(f'{e1.get_type_of_enemy()} wins!')
    else:
        print(f'{e2.get_type_of_enemy()} wins!')

def hero_battle(hero: Hero, enemy: Enemy):

    while hero.health_points > 0 and enemy.health_points > 0:
        print('------------')

        enemy.special_attack()

        print(f'Hero: {hero.health_points} HP left')
        print(f'{enemy.get_type_of_enemy()}: {enemy.health_points} HP left')
        enemy.attack()
        hero.health_points -= enemy.attack_damage
        hero.attack()
        enemy.health_points -= hero.attack_damage

    print('------------')
    if hero.health_points > 0:
        print('Hero wins!')
    else:
        print(f'{enemy.get_type_of_enemy()} wins!')

zombie = Zombie(10, 1)
ogre = Ogre(20, 3)

battle(zombie, ogre)

zombie = Zombie(10, 1)
hero = Hero(10, 1)
weapon = Weapon('Sword', 5)
hero.weapon = weapon
hero.equip_weapon()
hero_battle(hero, zombie)

