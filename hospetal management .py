class patients:
    def __init__(self):
        self.name=input("Enter your name >>")
        self.age=int(input("Enter your age >>"))

class pementblock:
    def __init__(self):
        self.__pement=0

    def pement_(self):
        amount = int(input("pay the amount"))
        self.__pement += amount
        print(f'you pay {amount} amount')

    def get_pement(self):
        return self.__pement


class booking(patients,pementblock):
    def __init__(self):
        patients.__init__(self)
        self.__booking=0
    def book(self):
        n=30-self.__booking
        print(f" remaining steats are {n}")
        place=int(input(f"Enter how many seats you book (only {n} number of seats is allowed) >>"))
        if n>=place:
            self.__booking +=place
            c=pementblock()
            print(f"you pay the amount {n * 120}")
            c.pement_()
            print(f" {place} seats are successfully  booked")
        else:
            print(f" seats are  not available")
            exit()
    def get_book(self):
        return  self.__booking


class docter:

    def docter():
        print("1,Dr pattile as a dentist surgeons")
        print("2,Dr sunil as a  fear  surgeons")
        print("3,Dr poorvaj  as a braine surgeons ")
        print("4,Dr sonu  as a  pediatrician surgeons")
        print("5,Dr nagesh as a obstetrician surgeons")

        option=int(input("enter your which block docter you meat>>\n"))
        match option:
            case 1:
                print("Dr pattile avilabel in coming at 8:30 AM")

            case 2:
                print("Dr sunil avilabel in coming at 10:30 AM")
            case 3:
                print("Dr poorvaj avilabel in coming at 1:30 PM")
            case 4:
                print("Dr sonu avilabel in 8:30 AM to 5 :30 PM")
            case 5:
                print("Dr nagesh  avilabel in coming at 7:30 PM to 5 :30 AM")
            case _:
                print("enter valied option try again")
                docter.docter()
        try:
            key=int(input("if you take the apppointement number 1 else enter 2>>>"))
        except ValueError:
            print("enter only number 1 or 2 ,alphabetical latters are not accepted")

        if key==1:
            book=int(input("if you book the  sites enter 1 else enter 2 >>"))
            if book==1:
                q=booking()
                q.book()
            elif book==2:
                print("OK BYEEE=")
            else:
                print("valide option try again")

        elif key==2:
            print("ok bye.........")
        else:
            print("enter only number 1 or 2 ,latters are not accepted")



print("======== WELL COME TO MY HOSPITAL ========")
print("your a patient enter option 1 else enter option 2")
try:
    option=int(input("enter option >>"))
    match option:
        case 1:
            docter.docter()
        case _:
            exit()
except ValueError:
    print("enter only numbers,alphabetical latters are not accepted")







