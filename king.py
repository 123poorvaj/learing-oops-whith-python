class king:
    def __init__(self):
        self.place_name=input("enter the place name >> ")
        self.king_name=input("enter the king name >> ")
        self.members=0

    def detaile(self):
        print(f'palce name is {self.place_name} king name is {self.king_name}')

class add(king):
    def add(self):
        n=int(input("how many member you want to add>> "))
        for i in range(n):
            self.members+=1
        print(f'member {self.members}')


c=add()
d=add()
#e=add()
c.add()
#e.add()
d.add()