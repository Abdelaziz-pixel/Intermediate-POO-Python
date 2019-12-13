"""Exercices 2"""

from véhicule import Véhicule

class Bus(Véhicule):

    étages = (1, 2)

    def __init__(self, nombre_étages):
        #self.__init__.Voiture()
        self.nombre_étages = nombre_étages

    @property
    def nombre_étages(self):
        return self.__nombre_étages

    @nombre_étages.setter
    def nombre_étages(self, nombre_étages) :
        if 1 == nombre_étages or 2 == nombre_étages:
            self.__nombre_étages = nombre_étages
        else :
            self.__nombre_étages = False

m = Bus(4)
print(m.nombre_étages)

    