# creat a parameter class shape with a method drow() that print "Drowing shape".
# create a childe class cricle that overrides drow() to print (" drowing circle").

class shape:
    def drow(self):
        print("Drowing shape ")

class circle(shape):
    def drow(self):  #overriding method
        print("Drowing cricle")

sp=shape()
sp.drow() #drowing shape
dp=circle()
dp.drow()  # both drowing shape and drowing circle.