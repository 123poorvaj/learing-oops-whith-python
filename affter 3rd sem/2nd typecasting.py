#----------type casting--------------------
from ctypes.wintypes import DOUBLE

x='3' #string are always inside the quats
print(type(x))
y=int(x) #sting to int
print(type(y))
z= float(y)
print(type(z)) #string to float
d=3.4
print(type(d))
c=str(d)  #float to string
print(type(c))

t=str(y) #int to string


