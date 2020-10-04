import random

class Character:
    def __init__(self, hp, atk, name='Player', level=1):
        self.level = level
        self.exp = 10 * (level - 1)

        factor = 1.1 ** (level - 1)
        self.hp = int(factor * hp)
        self.atk = int(factor * atk)
        self.name = name

    def attack(self, other):
        other.hp = max(0, other.hp - self.atk)

    def gain_exp(self, amount):
        print('> %s mendapat %d exp!' % (self.name, amount))
        self.exp += amount

class Knight(Character):
    def __init__(self, hp=100, atk=20, level=1, name='Knight'):
        super(Knight, self).__init__(
            hp=hp,
            atk=atk,
            level=level,
            name=name
        )

class Archer(Character):
    def __init__(self, hp=80, atk=30, level=1, name='Archer'):
        super(Archer, self).__init__(
            hp=hp,
            atk=atk,
            level=level,
            name=name
        )
