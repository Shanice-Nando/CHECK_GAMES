import random

class card :
    #definition d'une carte
    def __init__(self,val,form,color,penality):
        self.value = val
        self.form = form
        self.colors= color
        self.penalitys=penality


    def name_card (self):
        return f"{self.value}  de  {self.form}" 
class cards:
    def __init__(self):
       values=[str(v) for v in range(2,11)] + ["Valet","Dame","Roi","As","Joker"]
       forms={
          "Bs":"Biscuit",
          "Mn": "Macabo-Noir",
          "Cr": "Coeur-Rouge",
          "Ar": "Arachide"
       }
       
       
       self.cards=[]

      
       for form in forms.values():
           for val in values:
                 Color=None
                 penality=0
                 if val =="7":
                     penality=2
                 elif val=="Joker":
                     penality=4   
                     Color=["Red","Black"]
                       
                 self.cards.append(card(val,form,Color,penality))
    def Mix (self):
        random.shuffle(self.cards)
    def Display (self):
       for card in self.cards:
            print(card.name_card())
Action=None
Action=cards()
Action.Mix()
Action.Display()
