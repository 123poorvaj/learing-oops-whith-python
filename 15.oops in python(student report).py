class student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
        self.__marks={}
    def get_mark(self):
        return self.__marks

    def add_mark(self,sub,mark):
        self.__marks[sub]=mark

    def calculate_avrage(self):
        avareg=sum(self.__marks.values())/len(self.__marks)

        return avareg
    def his_pass(self):
          has_pass=all(mark>35 for mark in self.__marks.values())
          if has_pass:
              print(f"{self.name} has pass")
          else:
              print(f"{self.name} has fail")
    def grade(self):
        avareg=self.calculate_avrage()
        print(f"{avareg}" )
        if avareg>=90:
            print(f"{self.name} grade is 90% A grade")
        elif avareg>=80:
            print(f"{self.name} grade is 80% B grade")
        elif avareg<=70:
            print(f"{self.name} grade is 70% C grade")



s1=student("kisu",1)
s2=student("king",2)
s1.add_mark("kannada",67)
s1.his_pass()
s1.grade()
