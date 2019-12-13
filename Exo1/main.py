"""Exercices 1"""

"""importing the Clio class from the clio files"""
from clio import Clio

"""script launch"""
if __name__ == "__main__":

    """call and display of the Clio class chekprice method"""
    m = Clio(3, "black", 1234258)
    print(m.checkprice())