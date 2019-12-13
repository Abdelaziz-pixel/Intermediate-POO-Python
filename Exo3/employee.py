"""Exercices 3"""

from person import Person

class Employee(Person):

    # statuts = {1 = "employé",
    #            2 = "technicien",
    #            3 = "manager",
    #            4 = "cadre"}

    def __init__(self, nom, prénom, age, statut):
        self.statut = statut
        super().__init__(nom, prénom, age)