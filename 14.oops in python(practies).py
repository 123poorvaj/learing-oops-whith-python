


class student:
    def __init__(self,name,city,fees=0):
        self.name=name
        self.city=city
        self.fees=fees



class amount(student):
    def __init__(self):
        self.amount=int(input("pay your fees greater that one lack"))
        if self.amount>100000:
            self.fees+=self.amount
            print("your fees is sucessfully deposite\nupdated fees : ",self.fees)
        else:
            self.fees=115956-self.amount
            print("your fees is less than 1 lack pay balensed fees on next time",self.fees)




class cet(student):
    def gov_fees(self):
        print("congratulations your selected  my college thru the cet")
        print("your total fees is 115956")
        print("if you intrested to adimition to my college enter option 1 else enter option 2:")
        self.option = int(input("enter your option: "))
        if self.option==1:
            print("intruction :\nyour very locky to selet the college: pay amount")
            amount()
        else:
            print("you miss the great opertunity")



b=student("pooja","hebbalu")
s1=cet(b.name,b.city)
s1.gov_fees()



