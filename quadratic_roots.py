a=int(input("Enter first coefficient:"))
b=int(input("Enter second coefficient:"))
c=int(input("Enter third coefficient:"))
import math
d=(b*b)-(4*a*c)
if d<0:
    print("The roots are imaginary")
elif d==0:
    x=((-b)/(2*a))
    print("The roots are equal",x,",",x)
else:
    m=(math.sqrt(d)/(2*a))
    x1=int((-b)+m)
    x2=int((-b)-m)
    print(x1,x2)