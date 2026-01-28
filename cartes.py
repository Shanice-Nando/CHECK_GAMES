import random

class Card :
    #definition d'une carte
    def __init__(self,val,form,color,penality):
        self.value = val
        self.form = form
        self.colors= color
        self.penalitys=penality
    def name_card (self):
        if self.form == "Joker":
            return self.value
        return f"{self.value}  of  {self.form}" 
class Cards:
    def __init__(self):
       values=[str(v) for v in range(2,11)] + ["Valet","Dame","King","As"]
       forms={
          "Cs":"Cookies",
          "Bc": "Black-Cocoyam",
          "Rh": "Red-Heart",
          "Ps": "Peanuts"
       }
       self.Cards=[]
       for form in forms.values():
           for val in values:
                 Color=None
                 penality=0
                 
                 if val =="7":
                     penality=2
                 elif val=="Joker":
                     penality=4 
                     Color=["Red","Black"]
                       
                 self.Cards.append(Card(val,form,Color,penality))

       self.Cards.append(Card("Joker Red","Joker","Red","4"))
       self.Cards.append(Card("Joker Black","Joker","Black","4"))
           
    def Mix (self):
        random.shuffle(self.Cards)
    def Display (self):
       for card in self.Cards:
            print(card.name_card())
Action=None
Action=Cards()
Action.Mix()
Action.Display()

print(f"\nCards from the deck : {len(Action.Cards)}")
