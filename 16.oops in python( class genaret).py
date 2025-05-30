class classroom:
    def __init__(self,class_name,section):
        self.class_name=input("Enter class name: ")
        self.section=input("Enter section: ")
        self.__student={}

    def add_student(self):
        n=int(input("Enter how many student you want to add>> "))

        for i in range(n):
            self.name=(input("Enter student name>> "))
            self.roll_no=int(input("Enter student roll no>> "))
            self.__student[self.roll_no]=self.name
    def get_student(self):
        print(f" {sorted(self.__student.items())}")


print("===========this is classroom creating game===========")
print("you like to paly  game enter option 1 else enter option 2")
option=int(input("enter your option>>"))
if option==1:
    c=classroom("classroom","classroom")
    print("       do you like to add students?           " )
    print("    enter option 1 else enter option 2        ")
    choise=int(input("enter your option>>"))
    if choise==1:
        c.add_student()
        c.get_student()
    elif choise==2:
        print("               you miss the next intreting things        ")
else:
    print("                   you miss the next intreting things        ")