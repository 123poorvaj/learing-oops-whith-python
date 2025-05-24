#              method overloading
#  wire a class calculater whit a method multiple(). 
# allow it to take .allow ie take ethire two or three arguments to multiply two or three number#

class calculater:
    def multiply(self,a,b,c=0): 
        return a*b*c #handel both 2 & 3 parameter cases

num=calculater()
print(num.multiply(56,78)) #two arguments
print(num.multiply(45,67,78)) #three arguments
