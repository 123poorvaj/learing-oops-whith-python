#from sys import displayhook


def menu():
    print("====grocery store====")
    print("1. Add item\n2. Delete item\n3. View item\n4. Exit")

def addItem():
   n=int(input("how many items do you want to add?>> "))
   for i in range(n):
       key=input("enter item name>>")
       value=int(input("enter item price>>"))
       store[key]=value
   print(store)

def DELETE():
    n=int(input("how many items do you want to delete>>"))
    key=(input("enter which one you want to deleted item name>>"))
    del store[key]
    print(store)
def view():
    print("===items name===")
    print(store)

store = {"KI":56,"GI":45}
print(store)


while(True):
    menu()
    option = int(input("enter your option>>"))

    if option==1:
        addItem()
    elif option==2:
        DELETE()
    elif option==3:
        view()
    elif option==4:
        print("Exit")
        break
    else:
        print(" your option is Invalid option ,try again")




