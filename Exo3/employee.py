"""Exercices 3"""

"""importing the Person class from the person files"""
from person import Person

"""class named Employee"""
class Employee(Person):

    """constructor with for arguments"""
    def __init__(self, nom, prénom, age, statut):
        self.statut = statut
        super().__init__(nom, prénom, age)