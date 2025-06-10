try:
   a=int(input("enter a value>>"))
   b=int(input("enter b value>>"))
except ValueError:
    print("enter only integer value")
    exit()

print("======== simple calculater ========== ")
print("1,add\n 2,sub \n 3,maltiply \n 4,division\n")
key=int(input("enter your option>>"))
match key:
    case 1:
        print(f"adition is {a + b}")
    case 2:
        print(f"substraction is {a-b}")
    case 3:
        print(f"maltiplication  is {a*b}")
    case 4:
        print(f"division is {a/b}")
    case _:
          print("enter valied option try again")
