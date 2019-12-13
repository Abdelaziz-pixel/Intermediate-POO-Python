"""Exercices 3"""

from customer import Customer
from employee import Employee
from product import Product

if __name__ == "__main__":

    c = Customer("charles", "chalgoumi", 39, "vélo", 100)
    customer = ("Idendités complétes du client:\n nom: {}\n prénom: {}\n age: {} ans\n panier: {}\n montant: {}€".format(c.nom, c.prénom, c.age, c.panier, c.montant))
    print(customer)
    print("-----------------------------------------------------")
    e = Employee("boules", "praliné", 24, "cadre")
    employe = ("Idendités complétes de l'employé:\n nom: {}\n prénom: {}\n age: {} ans\n statut: {}".format(e.nom, e.prénom, e.age, e.statut))
    print(employe)




    