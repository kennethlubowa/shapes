from abstact import Shapes
import math
        
class Triangle(Shapes):
    
    def __init__(self,calc,unit):
        super().__init__(calc,unit)
        
        Triangle.typ=int(input("\n\n\t\t1.ISOSCELES  2.EQUILATERAL  3.RIGHT-ANGLED  "))
        if Triangle.typ > 3:
            print("\n\n\t\tINVALID CHOICE...TRY AGAIN!!")
            Triangle.__init__(self,calc,unit)
        else:    
            Triangle.base=float(input("\n\n\t\tENTER BASE:  "))
            Triangle.height=float(input("\n\n\t\tENTER HEIGHT:  "))
            Triangle.hyp=float(input("\n\n\t\tENTER HYPOTENUSE:  "))
        
    def Area(self):
        return (0.5)*self.base*self.height
    
    def Perimeter(self):
        ans=0
        if Triangle.typ==1:  #two of the sides are equal
            ans=self.base+(2*self.height)
            
        elif Triangle.typ==2: #all sides are equal
            ans=self.base*3
            
        else: #all sides are of different lengths
            ans=self.base+self.height+self.hyp
            
        return ans            
    
    def Volume(self):
        return Triangle.Area(self)*self.height    
    
class Circle(Shapes):
    
    def __init__(self,calc,unit):
        super().__init__(calc,unit)
        
        Circle.rad=float(input("\n\n\t\tENTER THE RADIUS:  "))    
        
    def Perimeter(self):
        return 2*round(math.pi,4)*self.rad
    
    def Volume(self):
        return (4/3)*round(math.pi)*pow(self.rad,3)    
    
    def Area(self):
        return round(math.pi,4)*pow(self.rad,2)   