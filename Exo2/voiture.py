"""Exercices 2"""

"""import of the Véhicule class from the véhicule files"""
from véhicule import Véhicule

"""class named Car which inherits from Vehicle class"""
class Voiture(Véhicule):
    
    """Voiture class attribute"""
    nombre_portes = (3, 5)

    """Bus class constructor with three arguments"""
    def __init__(self, nombre_portes, immatriculation, couleur):
        self.nombre_portes = nombre_portes
        super().__init__(immatriculation, couleur)
        
    """@property decorator allows us to define properties 
    easily without calling the property() function manually"""
    @property
    def nombre_portes(self):
        return self.__nombre_portes

    """This is how we can define a property and its getter and setter methods"""
    @nombre_portes.setter
    def nombre_portes(self, nombre_portes):
        if 3 == nombre_portes or 5 == nombre_portes:
            self.__nombre_portes = nombre_portes
        else:
            self.__nombre_portes = False

