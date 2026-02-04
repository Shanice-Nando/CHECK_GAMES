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

print(f"la carte du centre est:{centerCards[0].name_card()}")

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


    for joueur in listPlayer:
        listCardpossibletoPlay = []
        for carte in joueur.listCardsPlayer:
            if carte.value == centerCards[0].value or carte.form == centerCards[0].form:
                listCardpossibletoPlay.append(carte)
            if carte.form == "Joker" and carte.colors == centerCards[0].colors:
                listCardpossibletoPlay.append(carte)

        if len(listCardpossibletoPlay) == 0:
            print(f"{joueur.namePlayer} n'a pas de cartes possibles à jouer")
            joueur.drawCards(1)
        else:
            print(f"{joueur.namePlayer}, c'est à toi de jouer.Fais ton choix parmis les cartes suivantes:")
            for n in range(0,len(listCardpossibletoPlay)):
                print(f'{n}- {listCardpossibletoPlay[n].name_card()}')
            print(f'{n+1}- Piocher')
            print()
            print("Ton choix(seul l'index est necessaire):")
            while True:
                try:
                    choice = int(input())
                    if choice < 0 or choice > n+1:
                        raise ValueError
                    break
                except ValueError:
                    print(f"Entre une valeur entre 0 et {n+1}")
            if choice < len(listCardpossibletoPlay):
                joueur.playACard(joueur.listCardsPlayer.index(listCardpossibletoPlay[choice]))
            else:
                joueur.drawCards(1)
        print(f"la carte du centre est:{centerCards[-1].name_card()}")






