def madhu():
    ln=len(king_name)
    for my_name in range(ln):
        print(f"{king_name} was  a king of the kindom")
def ranju():
    Queen_name="RANJU"
    condition=0
    while(True):
        condition+=1
        print(f"{Queen_name} was a queen of the kindom ")
        if condition==3:
            break
king_name="MADHU"
Queen_name="RANJU"
print("1-king name , 2-queen name")
option=(input("enter your option>>"))
if option==1:
    madhu()
elif option==2:
    ranju()
else:
    print("your option is wrong")