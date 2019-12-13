"""Exercices 1"""

"""class named clio"""
class Clio():

    """attributes of the class clio"""
    price_range = [8000, 30000]
    price = 20000
    doors = (3, 5)
    colors = {
        "black" : 1234258,
        "blue" : 14255,
        "green" : 143582,
        "red" : 134625952,
        "white" : 125452
        }    

    """constructor with 3 arguments"""
    def __init__(self, number_doors, color, color_number):
        self.__number_doors = number_doors
        self.__color = color
        self.__color_number = color_number    

    """@property decorator allows us to define properties 
    easily without calling the property() function manually"""
    @property 
    def number_doors(self):
        return self.__number_doors    
        
    """This is how we can define a property and its getter and setter methods"""
    @number_doors.setter
    def number_doors(self, number_doors) :
        if number_doors in Clio.doors :
            self.__number_doors = number_doors
        else :
            raise ValueError    

    """@property decorator allows us to define properties 
    easily without calling the property() function manually"""
    @property 
    def color_number(self):
        return self.__color_number   
        
    """This is how we can define a property and its getter and setter methods"""
    @color_number.setter
    def color_number(self, color_number) :
        if color_number in Clio.colors.value() :
            self.__color_number = color_number
        else :
            raise ValueError 
    
    """@property decorator allows us to define properties 
    easily without calling the property() function manually"""
    @property 
    def color(self):
        return self.__color    
        
    """This is how we can define a property and its getter and setter methods"""
    @color.setter
    def color(self, color) :
        if color in Clio.colors.key() :
            self.__color = color
        else :
            raise ValueError     

    """The decorator @classmethod can be applied to a method of a class. 
    This decorator will allow us to call this method using the class name 
    instead of the object"""
    @classmethod
    def checkprice(cls):
        if cls.price in range (8000, 30000):
            return cls.price
        else :
            raise ValueError
