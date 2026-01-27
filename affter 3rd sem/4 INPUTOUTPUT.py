#Inputs and out puts
'''
print('my name is poorvaj')#out put

name=input("enter your name>> ") #takes input from users
#syntax of exception handling
    try:
        age=int(input("Enter your age>> "))#input with type casting
        print(f"my name is {name} and age is {age}")
        break
    except ValueError:
        print("enter age proprly")
    finally:print("program exicute")



from unittest import case

from IPython.terminal.shortcuts.auto_match import braces

#age finding code
'''
name=input("Enter your name>> ")
for i in range(5):
    try:
        key=int(input("1.find brith year\n2.find age\n>> "))
        match key:
            case 1:
                    date_of_birth=int(input("Enter your Age>> "))
                    break
            case 2:
                    date_of_birth=int(input("Enter your year of Birth>> "))
                    break
            case _:
                print("enter correct value")
    except ValueError:

        if(i==3):
            print("this is last warning enter interger value")
        else:
            print("Enter numerical value...")

age= 2026 -(date_of_birth)
b=str(date_of_birth)
print("============Result==================")
if (len(b)<=3):
    print(f"Hi {name} your birth year is {age}")
else:
    print(f"Hi {name} your age is {age}") #farmated string