
'''class Human:
    def __init__(self, name, age, h, w):
        self.name = name
        self.age = age
        self.hight = h
        self.weidht = w


man = Human('Ivan',15, 175,88)
women = Human('ann',32, 165,75)
print(man.age)
print(women.name)'''
from random import randint

'''class Car:
    def __init__(self, color, speed, fell, mark):
        self.color = color
        self.speed = speed
        self.fell = fell
        self.mark = mark


    def getinfo(self):
        print(f'color: {self.color}')



car1 = Car('red', 80, 95, 'BMW')
car1.getinfo()

car2 = Car('blue', 180, 98, 'lada')
car2.getinfo()

#print(car1.mark)'''

'''class Rectangle:
    def __init__(self, w, h):
        self.hight = h
        self.wight = w

    def calc1(self):
        print(f'S = {self.wight * self.hight}')

    def calc2(self):
        print(f'P = {(self.hight + self.wight) * 2}')


rec1 = Rectangle(22, 12)
rec1.calc1()
rec1.calc2()'''


'''class Cart:

    def __init__(self, money, pin):
        self.money = money
        self.pincode = pin

    def add(self, moneyplus):
        self.money += moneyplus
        print(f'your balance: {self.money}')

    def buy(self, price):
        taskcod = int(input('Your PIN code: '))
        if taskcod == self.pincode:
            if self.money >= price:
                self.money -= price
                print('You buy a toy!!!')
                print(f'your balance: {self.money}')
            else:
                print('No money')
        else:
            print('wrong PIN')

cart1 = Cart(200, 5643)
cart1.buy(100)'''

'''class Game:
    def __init__(self, hp1, hp2):
        self.health1 = hp1
        self.health2 = hp2

    def hit1(self, hitpower):
        if self.health1 <= 0:
            print('Player 1 loss')
        elif self.health2 <= 0:
            print('Player 2 loss')
        else:
            self.health1 -= hitpower


    def hit2(self, hitpower):
        if self.health1 == 0:
            print('Player 1 loss')
        elif self.health2 == 0:
            print('Player 2 loss')
        else:
            self.health2 -= hitpower


game = Game(500, 500)
for x in range(3):
    game.hit1(40)
    game.hit2(50)
    game.hit1(40)
    game.hit1(40)
    game.hit2(50)
    game.hit1(40)'''

import random
class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.power = random.randint(5, 15)

    def attack(enemmy, self):
        enemmy.hp -= self.power
        print('Attack')

    def buff(self):
        if randint(0, 1) == 1:
            b = randint(1,3)
            self.power += b
            print(f'Бафф прошел, игрок получил +{b} к силе!')
        else:
            print('Бафф не прошел')

    def regen(self):
        if randint(0, 1) == 1:
            b = randint(1,5)
            self.hp += b
            print(f'реген прошел, игрок получил +{b} к здоровью!')
        else:
            print('реген не прошел')



        




