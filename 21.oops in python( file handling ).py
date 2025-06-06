name=input("enter the student name")
marks=input("enter your marks")
with open("marks.txt","w") as file:
    v=file.write(f"{name} -{marks}")
    print(v)