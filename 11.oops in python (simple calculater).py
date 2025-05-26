def add():
    return a+b

def divid():
    return a/b

def multi():
    return a*b

def sub():
    return a-b

print("simple claculater")
print("1.add\n2.divid\n3.multiply\n4.sub\n5.exite")
a=int(input("enter value of a>>"))
b=int(input("enter value of b>>"))
option=int(input("enter your option>>"))
if option==1:
    print(add())
elif option==2:
    print(divid())
elif option==3:
    print(multi())
elif option==4:
    print(sub())
elif option==5:
    print("Thank you for using me: goodbye")



