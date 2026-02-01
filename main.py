from cartes import *
from Player import *

player1 = Player("", [])
player2 = Player("", [])

listPlayer = [player1,player2]

def getName():
    player1.namePlayer = str(input("Enter the player's Username 1:"))
    player2.namePlayer = str(input("Enter the player's Username 2:"))
    if player1.namePlayer.strip() == "" or player1.namePlayer.strip() == "":
        print("names required. Try again!")
        getName()


print(f"START OF THE GAME: {player1.namePlayer} vs {player2.namePlayer}")

Action.Mix()
centerCards = []

player1.drawCards(4)
player2.drawCards(4)

centerCards.append(Action.Cards[0])
Action.Cards.pop(0)

isPartyFinish = False

while isPartyFinish == False:
    if len(player1.listCardsPlayer) == 0 or len(player2.listCardsPlayer) == 0:
        isPartyFinish = True
        for player in listPlayer:
            if len(player.listCardsPlayer) == 0:
                print(f"END OF THE GAME. Winner: {player.namePlayer}")
        break

    for player in listPlayer:
       print(f'Cartes en main de {player.namePlayer}:')
       for card in player.listCardsPlayer:
           print(card.name_card())




