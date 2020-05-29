'''
    program: attack calculator
    author: builtbyjosh
    created: 5-27-2020
'''


import random


class Enemy:
    hp = 200
    
    def __init__(self, atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh

    def get_atk(self):
        print("atk is", self.atkl)

    def get_hp(self):
        print("HP is", self.hp)


enemy1 = Enemy(40, 49)
enemy1.get_atk()
enemy1.get_hp()

enemy2 = Enemy(75, 90)
enemy2.get_atk()
enemy2.get_hp()

# player_hp = 260
# enemy_atkl = 60
# enemy_atkh = 80

# while player_hp > 0:
#     dmg = random.randrange(enemy_atkl, enemy_atkh)
#     player_hp -= dmg

#     if player_hp <= 30:
#         player_hp = 30

#     print(f"Damage of {dmg} taken. Player HP is {player_hp}")

#     if player_hp > 30:
#         continue

#     print("Player has low health. Go to hospital")
#     break