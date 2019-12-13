"""Exercices 3"""

from person import Person

class Customer(Person):

    Panier = []
    Montant = 0

    def __init__(self, nom, prénom, age, panier, montant):
        self.panier = panier
        self.montant = montant
        super().__init__(nom, prénom, age)
        
 


    