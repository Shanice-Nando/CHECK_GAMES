from cartes import *
from Player import *

player1 = Player("", [])
player2 = Player("", [])

try:
    player1.namePlayer = str(input("Entrer le pseudo du joueur 1:"))
    player2.namePlayer = str(input("Entrer le pseudo du joueur 2:"))
except:
    print("Une erreur est survenue")

print(f"DEBUT DE LA PARTIE: {player1.namePlayer} vs {player2.namePlayer}")

Action.Mix()
centerCards = []

player1.drawCards(4)
player2.drawCards(4)

centerCards.append(Action.cards[0])
Action.cards.pop(0)


