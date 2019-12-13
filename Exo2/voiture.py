"""Exercices 2"""

#from véhicule import Véhicule

class Voiture():
    
    nombre_portes = (3, 5)

    def __init__(self, nombre_portes):
        #self.__init__.Véhicule
        self.nombre_portes = nombre_portes

    @property
    def nombre_portes(self):
        return self.__nombre_portes

    @nombre_portes.setter
    def nombre_portes(self, nombre_portes):
        if 3 == nombre_portes or 5 == nombre_portes:
            self.__nombre_portes = nombre_portes
        else:
            self.__nombre_portes = False

v = Voiture(2)
print(v.nombre_portes)
