class book:
    def __init__(self,name):
        self.name=name
    def details(self):
        print(f"book details name {self.name}")

class pint:
   def __init__(self):
       self.print=input("enter a book name")
   def details(self):
       print(f"pint details name {self.print}")

class detailse:
    def __init__(self,name):
        self.name=input("enter a book name>>")
    def details2(self):
        print(f"details name {self.name}")


c=detailse("name")
c.details2()




