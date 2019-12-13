"""Exercices 2"""

"""import of the Bus class from the bus files"""
from véhicule import Véhicule

"""class named bus"""
class Bus(Véhicule):

    """bus class attribute"""
    étages = (1, 2)

    """Bus class constructor with two arguments"""
    def __init__(self, nombre_étages, immatriculation, couleur):
        self.nombre_étages = nombre_étages
        super().__init__(immatriculation, couleur)

    """@property decorator allows us to define properties 
    easily without calling the property() function manually"""
    @property
    def nombre_étages(self):
        return self.__nombre_étages

    """This is how we can define a property and its getter and setter methods"""
    @nombre_étages.setter
    def nombre_étages(self, nombre_étages) :
        if 1 == nombre_étages or 2 == nombre_étages:
            self.__nombre_étages = nombre_étages
        else :
            self.__nombre_étages = False


    