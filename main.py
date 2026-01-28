from cartes import *
from Player import *

player1 = Player("", [])
player2 = Player("", [])

try:
    player1.namePlayer = str(input("Enter the player's Username 1:"))
    player2.namePlayer = str(input("Enter the player's Username 2:"))
except:
    print("An error has occurred")

print(f"START OF THE GAME: {player1.namePlayer} vs {player2.namePlayer}")

Action.Mix()
centerCards = []

player1.drawCards(4)
player2.drawCards(4)

centerCards.append(Action.Cards[0])
Action.Cards.pop(0)


