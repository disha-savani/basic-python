class Complex:
    def __init__(self,r,i):
        self.real=r
        self.imaginary=i

    def __add__(self,c):
        return Complex(self.real+c.real , self.imaginary+c.imaginary)

    def __mul__(self,d):
        mulreal=self.real*d.real - self.imaginary*d.imaginary
        mulimg=self.real*d.imaginary + self.imaginary*d.real
        return complex(mulreal,mulimg)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"
    

c1=complex(3,2)
c2=complex(1,7)
print(c1+c2)
print(c1*c2)