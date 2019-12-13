"""Exercices 3"""

"""importing the Person class from the person files"""
from person import Person

"""class named Customer"""
class Customer(Person):

    """attributes of the class Customer"""
    Panier = []
    Montant = 0
    
    """constructor with five arguments"""
    def __init__(self, nom, prénom, age, panier, montant):
        self.panier = panier
        self.montant = montant
        super().__init__(nom, prénom, age)
        
 


    