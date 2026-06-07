#python in build string methods

'''
string is sequence of charecter,later, etc enclosed is quotes
is called string 
'''

#example
a='poo#56'
print(a)
print(type(a)) #type in bild function use to check the type of the variable or value

'''1.upper()
it converts all later to uppercase
'''
a='poorvaj m gowda'
b=a.upper()
print("uppercase>> ",b)

'''2.lower()
it converts all later to lowercase
'''

c=a.lower()
print("Lowercase>> ",c)

'''3.capitalize()
it makes only frist later Uppercase.
'''
d=a.capitalize()
print("capitalize>> ",d)

'''4.title()
its makes each word frist later is capital 
'''
e=a.title()
print("titel>> ",e)

'''5.count()
its helps to count how many times the later parsent in the string
'''
f=a.count('o')
print("count>> ",f)

g=a.count('rv')
print(f"rv prasent {g} times in 'poorvaj' ")