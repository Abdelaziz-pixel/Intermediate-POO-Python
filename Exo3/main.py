"""Exercices 3"""

"""importing the Customer class from the customer files"""
from customer import Customer
"""importing the Employee class from the employee files"""
from employee import Employee
"""importing the Product class from the product files"""
from product import Product

"""script launch"""
if __name__ == "__main__":

    """we attribute values to the attributes of the Customer 
    class and we measure them with the format method"""
    c = Customer("charles", "chalgoumi", 39, "vélo", 100)
    customer = ("Idendités complétes du client:\n nom: {}\n prénom: {}\n age: {} ans\n panier: {}\n montant: {}€".format(c.nom, c.prénom, c.age, c.panier, c.montant))
    print(customer)

    print("--------------------------------------------------------")

    """we attribute values to the attributes of the Employee 
    class and we measure them with the format method"""
    e = Employee("boules", "praliné", 24, "cadre")
    employe = ("Idendités complétes de l'employé:\n nom: {}\n prénom: {}\n age: {} ans\n statut: {}".format(e.nom, e.prénom, e.age, e.statut))
    print(employe)




    