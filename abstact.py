from abc import ABC, abstractmethod

class Shapes:
    
    calculation=None
    units=None
    def __init__(self,calculation,units):
        self.calculation=calculation
        self.units=units
    
    @abstractmethod
    def Perimeter(self):
        pass
    
    @abstractmethod
    def Area(self):
        pass
    
    @abstractmethod
    def Volume(self):
        pass 

shape = ["","SQUARE","RECTANGLE","RHOMBUS","PARALLELOGRAM","TRAPEZIUM","KITE","CUBE","CUBOID","CIRCLE","CYLINDER","TRIANGLE"]

mathe = ["","PERIMETER","AREA","VOLUME"]