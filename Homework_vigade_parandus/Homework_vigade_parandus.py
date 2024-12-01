from math import * # change from import * from math to from math import *
print("Ruudu karakteristikud")
a=float(input("Sisesta ruudu külje pikkus => ")) #' ' to " ",  float() added
S=a**2
print("Ruudu pindala", S)
P=4*a
print("Ruudu ümbermõõt", P)#''to "
di=a*sqrt(2)# math was not needed and sqrt had wrong spelling
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud")# extra ) deleted
b=float(input("Sisesta ristküliku 1. külje pikkus => "))#float() added
c=float(input("Sisesta ristküliku 2. külje pikkus => "))#float() added
S=b*c
print("Ristküliku pindala", S) #from print(Ristküliku pindala', S)  to print("Ristküliku pindala", S) 
P=2*(b+c)# added * between 2 and (b+c)
print("Ristküliku ümbermõõt", P)
di=sqrt(b*2+c*2)
print("Ristküliku diagonaal", round(di))# added ) in the end
print()
print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus => "))# '' '' changed to " " and added float(
d=2*r# added * between 2 and r
print("Ringi läbimõõt", d)
S=pi*r*2#deleted () near pi
print("Ringi pindala", round(S))
C=2*pi*r#added * between pi and 2, deleted () near pi
print("Ringjoone pikkus", round(C))# added ) at the end of the code
