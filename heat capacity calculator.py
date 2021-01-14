import math
from decimal import Decimal

coefficient = float(input("coefficient="))
A,B,C,D,E = input("Enter C1 to C5 separated by a space").split() 
C1, C2, C3, C4, C5 = float(A)*10**5, float(B)*10**5, float(C)*10**3,float(D)*10**5,float(E)
u = float(input("upper_bound="))
l = float(input("lower_bound="))
u_value = C1*u+C2*C3*(1/math.tanh(C3/u))-C4*C5*math.tanh(C5/u)
l_value = C1*l+C2*C3*(1/math.tanh(C3/l))-C4*C5*math.tanh(C5/l)
result = u_value - l_value
print('%.3f' % (result/10**6*coefficient), " kJ/mol")
