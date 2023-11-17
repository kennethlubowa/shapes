from abstact import mathe,shape
from threesided import *
from foursided import *

print("\n\n\t\t\tWELCOME TO THE SHAPE METRICS' CALCULATOR\n\n")

for i in range(50):
    try:
        choice = int(input("\t\t\t\t\t\tSELECTED SHAPE: \n\n\t\t1."+shape[1]+"  2."+shape[2]+"  3."+shape[3]+"  4."+shape[4]+"  5."+shape[5]+"  6."+shape[6]+"  7."+shape[7]+"  8."+shape[8]+"  9."+shape[9]+"\n\n\t\t"+"10."+shape[10]+"  11."+shape[11]+"\n\t\t\t\t"))
        
        if shape[choice]==shape[9]:
            mathe[1]="CIRCUMFERENCE"
    
    except IndexError as e:
        print("\n\n\t\t"+str(e).upper()+"....TRY AGAIN!!!\n\n") 
        continue   
    
    print("\n\n\t\tYOU CHOSE "+str(shape[choice]))    
    
    cal = int(input("\n\nCHOOSE: 1."+mathe[1]+"  2."+mathe[2]+"  3."+mathe[3]+"\n\t\t\t\t"))
    
    if cal==1:
        unit="UNITS"
    elif cal==2:
        unit="UNITS SQUARED"
    else:
        unit="UNITS CUBED"    
    if choice==1:
        square = Square(cal,unit) 
        if cal==1:
            ans=square.Perimeter()
        elif cal==2:
            ans=square.Area()
        else:
            ans=square.answer      
    elif choice==2:
        rectangle = Rectangle(cal,unit)
        if cal==1:
            ans=rectangle.Perimeter()
        elif cal==2:
            ans=rectangle.Area()
        else:
            ans=rectangle.answer    
    elif choice==3:
        rhombus = Rhombus(cal,unit)
        if cal==1:
            ans=rhombus.Perimeter()
        elif cal==2:
            ans=rhombus.Area()
        else:
            ans=rhombus.answer    
    elif choice==4:
        parallelogram = Parallelogram(cal,unit)
        if cal==1:
            ans=parallelogram.Perimeter()
        elif cal==2:
            ans=parallelogram.Area()
        else:
            ans=parallelogram.answer    
    elif choice==5:
        trapezium = Trapezium(cal,unit)
        if cal==1:
            ans=trapezium.Perimeter()
        elif cal==2:
            ans=trapezium.Area()
        else:
            ans=trapezium.answer    
    elif choice==6:
        kite = Kite(cal,unit)
        if cal==1:
            ans=kite.Perimeter()
        elif cal==2:
            ans=kite.Area()
        else:
            ans=kite.answer   
    elif choice==7:
        cube = Cube(cal,unit)
        if cal==1:
            ans=cube.Perimeter()
        elif cal==2:
            ans=cube.Area()
        else:
            ans=cube.Volume()    
    elif choice==8:
        cuboid = Cuboid(cal,unit)
        if cal==1:
            ans=cuboid.Perimeter()
        elif cal==2:
            ans=cuboid.Area()
        else:
            ans=cuboid.Volume()    
    elif choice==9:
        circle = Circle(cal,unit)
        if cal==1:
            ans=circle.Perimeter()
        elif cal==2:
            ans=circle.Area()
        else:
            ans=circle.Volume()    
    elif choice==10:
        cylinder = Cylinder(cal,unit)
        if cal==1:
            ans=cylinder.answer
        elif cal==2:
            ans=cylinder.Area()
        else:
            ans=cylinder.Volume()    
    elif choice==11:
        triangle = Triangle(cal,unit)
        if cal==1:
            ans=triangle.Perimeter()
        elif cal==2:
            ans=triangle.Area()
        else:
            ans=triangle.Volume() 

    if ans == str(ans):
        pass
    else:    
        print("\n\n\t\tTHE "+str(mathe[cal]+" OF THE "+str(shape[choice]+" IS "+str(ans)+" "+unit)))
        
    time = int(input("\n\n\t\tENTER 1 TO CONTINUE OR ANOTHER NUMBER TO ABORT:  "))
    if time!=1:
        break

print("\n\n\n\n")    