from main import Player
from game import Game

player1 = Player('ivan' , 20)
player2 = Player('Titan' , 20)

game = Game(player1, player2)

while game.run:
    game.info()
    game.gameround()