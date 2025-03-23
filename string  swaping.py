# >> this code is based converstion of string in capitl latter into small latter
# >>syntax (variable.lower())
def small_latter():
   print(a.lower())

#>> this code is based converstion of string in small latter into capittal latter
#>>syntax (variable.upper())
def capital_latter():
   print(b.upper())

##>> this code is based converstion of sring  both (capitl latter and small latter)
#>>syntax (variable.swapcase())
def swaping_latter():
   print(c.swapcase())


print("1-small,2-capital,3-swaping")
option=int(input("your option>>" ))
if option==1:
    a=(input("enter only capital latter>> "))
    small_latter()
elif option==2:
    b = (input("enter only small latter>> "))
    capital_latter()
elif option==3:
    c = (input("enter mix  latter>>"))
    swaping_latter()

