from cartes import *
from main import *

  ########### creation de la classe joueur ##########

class Player():
    def __init__(self, namePlayer, listCardsPlayer):
        self.namePlayer = namePlayer
        self.listCardsPlayer = listCardsPlayer
        self.listCardsPlayer = []

    def playACard(self, index):
        self.listCardsPlayer.pop(index)
        print(f"The player played {self.listCardsPlayer[index].name_card()}")
        centerCards.append(self.listCardsPlayer[index])

    def drawCards(self, number):
        for i in range(0, number):
            self.listCardsPlayer.append(Action.Cards[0])
            Action.Cards.pop(0)
