from abstact import Shapes
import math

class Cube(Shapes):
    
    def __init__(self,calc,unit):
        super().__init__(calc,unit)  
        
        Cube.side=float(input("\n\n\t\tENTER SIDE LENGTH:  "))
        
    def Perimeter(self):
        return self.side*12
    
    def Volume(self):
        return pow(self.side,3)    
    
    def Area(self):
        print("\n\n\t\tNOTE:THIS IS SURFACE AREA")
        return 6*pow(self.side,2)    
        
class Cuboid(Shapes):
    
    def __init__(self,calc,unit):
        super().__init__(calc,unit)   
        
        Cuboid.length=float(input("\n\n\t\tENTER LENGTH:  "))
        Cuboid.width=float(input("\n\n\t\tENTER WIDTH:  "))
        Cuboid.height=float(input("\n\n\t\tENTER HEIGHT:  ")) 
        
    def Perimeter(self):
        return 6*self.length*self.width
    
    def Volume(self):
        return self.length*self.width*self.height    
    
    def Area(self):
        return self.length*self.width    
        
class Cylinder(Shapes):
    
    def __init__(self,calc,unit):
        super().__init__(calc,unit)
        
        if calc==1:
            self.answer=Cylinder.Perimeter(self)
        else:
            Cylinder.radius=float(input("\n\n\t\tENTER RADIUS:  "))
            Cylinder.height=float(input("\n\n\t\tENTER HEIGHT:  "))    
        
    def Perimeter(self):
        print("\n\n\t\tIMPOSSIBLE TO CALCULATE THE PERIMETER OF A CYLINDER!")
        return "UNDETERMINABLE" 
    
    def Volume(self):
        return round(math.pi,4)*pow(self.radius,2)*self.height    
    
    def Area(self):
        fac1=2*round(math.pi,4)*self.radius*self.height #area of longer end
        fac2=2*round(math.pi,4)*pow(self.radius,2) #area of circular end
        return fac1+fac2
    
class Kite(Shapes):
    
    def __init__(self,calc,unit):
        super().__init__(calc,unit) 
        
        if calc==3:
            self.answer = Kite.Volume(self)
        else:    
            Kite.llength=float(input("\n\n\t\tENTER LONGER LENGTH:  "))
            Kite.slength=float(input("\n\n\t\tENTER SHORTER LENGTH:  ")) 
            Kite.ldiagonal=float(input("\n\n\t\tENTER LONGER DIAGONAL:  "))
            Kite.sdiagonal=float(input("\n\n\t\tENTER SHORTER DIAGONAL:  "))    
        
    def Perimeter(self):
        return 2*(self.slength+self.llength)
    
    def Volume(self):
        print("\n\n\t\tIMPOSSIBLE TO CALCULATE THE VOLUME OF A KITE!") 
        return "UNDETERMINABLE"  
    
    def Area(self):
        return 0.5*self.sdiagonal*self.ldiagonal    

class Parallelogram(Shapes):
    
    def __init__(self,calc,unit):
        super().__init__(calc,unit)
        
        if calc==3:
            self.answer=Parallelogram.Volume(self)
        else:        
            Parallelogram.length=float(input("\n\n\t\tENTER LENGTH:  "))
            Parallelogram.width=float(input("\n\n\t\tENTER WIDTH:  "))
            Parallelogram.height=float(input("\n\n\t\tENTER HEIGHT:  "))    
        
    def Perimeter(self):
        return 2*(self.length+self.width)
    
    def Volume(self):
        print("\n\n\t\tIMPOSSIBLE TO CALCULATE THE VOLUME OF A PARALLELOGRAM!")
        return "UNDETERMINABLE"    
    
    def Area(self):
        return self.length*self.height    
        
class Rectangle(Shapes):
    
    def __init__(self,calc,unit):
        super().__init__(calc,unit)
        
        if calc==3:
            self.answer=Rectangle.Volume(self)
        else:    
            Rectangle.leng = float(input("\n\n\t\tENTER THE LENGTH:  "))
            Rectangle.wid = float(input("\n\n\t\tENTER THE WIDTH:  "))    
        
    def Perimeter(self):
        return 2*(self.leng+self.wid)
    
    def Volume(self):
        print("\n\n\t\tIMPOSSIBLE TO CALCULATE THE VOLUME OF A RECTANGLE!") 
        return "UNDETERMINABLE" 
    
    def Area(self):
        return  self.wid*self.leng   

class Rhombus(Shapes):
    
    def __init__(self,calc,unit):
        super().__init__(calc,unit) 
        
        if calc==3:
            self.answer=Rhombus.Volume(self)
        else:    
            Rhombus.length=float(input("\n\n\t\tENTER LENGTH:  "))
            Rhombus.height=float(input("\n\n\t\tENTER HEIGHT:  "))   
        
    def Perimeter(self):
        return 4*self.length
    
    def Volume(self):
        print("\n\n\t\tIMPOSSIBLE TO CALCULATE THE VOLUME OF A RHOMBUS!")
        return "UNDETERMINABLE"     
    
    def Area(self):
        return self.length*self.height    

class Square(Shapes):
    
    def __init__(self,calc,unit):
        super().__init__(calc,unit) 
        
        if calc==3:
            self.answer=Square.Volume(self)
        else:    
            Square.leng = float(input("\n\n\t\tENTER THE LENGTH:  "))  
    
    def Perimeter(self): 
        return 4*self.leng
    
    def Volume(self):
        print("\n\n\t\tIMPOSSIBLE TO CALCULATE THE VOLUME OF A SQUARE!") 
        return "UNDETERMINABLE"  
    
    def Area(self):
        return self.leng*self.leng  
        
class Trapezium(Shapes):
    
    def __init__(self,calc,unit):
        super().__init__(calc,unit) 
        
        if calc==3:
            self.answer=Trapezium.Volume(self)
        else:        
            Trapezium.llength=float(input("\n\n\t\tENTER LONGER LENGTH:  "))
            Trapezium.slength=float(input("\n\n\t\tENTER SHORTER LENGTH:  ")) 
            Trapezium.height=float(input("\n\n\t\tENTER HEIGHT:  "))
            Trapezium.bend=float(input("\n\n\t\tENTER BEND:  "))       
        
    def Perimeter(self):
        return self.llength+self.slength+self.height+self.bend
    
    def Volume(self):
        print("\n\n\t\tIMPOSSIBLE TO CALCULATE THE VOLUME OF A TRAPEZIUM!") 
        return "UNDETERMINABLE"   
    
    def Area(self):
        return 0.5*self.height*(self.llength+self.slength)    