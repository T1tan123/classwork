
class Game:
    def __init__(self, p1 , p2):
        self.p1 = p1
        self.p2 = p2
        self.run = True

    def gameround(self):
        if self.p1.hp > 0 and self.p2.hp > 0:
            self.p1.buff()
            self.p1.regen()
            self.p1.attack(self.p2)
            self.p2.buff()
            self.p2.regen()
            self.p2.attack(self.p1)
        else:
            print('бой окончен')
            self.run = False


    def info(self):
        print(f'Здоровье {self.p1.name}: {self.p1.hp}')
        print(f'Power {self.p1.name}: {self.p1.power}')
        print(f'Здоровье {self.p2.name}: {self.p2.hp}')
        print(f'Power {self.p2.name}: {self.p2.power}')

