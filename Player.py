from main import*
from cartes import*

  ########### creation de la classe joueur ##########

class Player():
    def __init__(self, namePlayer, listCardsPlayer):
        self.namePlayer = namePlayer
        self.listCardsPlayer = listCardsPlayer
        self.listCardsPlayer = []

    def playACard(self, index):
        centerCards.append(self.listCardsPlayer[index])
        print(f"The player played {self.listCardsPlayer[index].name_card()}")
        self.listCardsPlayer.pop(index)
    def drawCards(self, number):
        for i in range(0, number):
            self.listCardsPlayer.append(Action.Cards[0])
            Action.Cards.pop(0)
        print(f"{self.namePlayer} a tiré {number} carte(s)")