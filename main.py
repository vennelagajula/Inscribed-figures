import math 
def area(n:int,r:int,shape:str)->float:
    diagonal = n * math.sqrt(2)
    diameter = diagonal - (2*r * (math.sqrt(2)+1))
    CIR = 3.14 * (diameter/2) ** 2
    SQR = (diameter/math.sqrt(2))**2
    if (shape == CIR):
        print(CIR)
    else:
        print(SQR)
 
   
n =int(input("enter side of a square:"))
r =int(input("enter radius of a circle:"))
shape = input("enter the required shape:")
area(n,r,shape)
