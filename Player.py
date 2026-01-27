from cartes import *

class Player():
    def __init__(self, namePlayer, listCardsPlayer):
        self.namePlayer = namePlayer
        self.listCardsPlayer = listCardsPlayer
        self.listCardsPlayer = []

    def playACard(self, index):
        self.listCardsPlayer.pop(index)
        print(f"le joueur a joué {self.listCardsPlayer[index]}")

    def drawCards(self, number):
        for i in range(0, number):
            self.listCardsPlayer.append(Action.cards[0])
            Action.cards.pop(0)