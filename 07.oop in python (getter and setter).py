# getter a class bankaccount with aprivate attribute balance.
# write a methode to retuieve the balance and a settermethod to update it ,
# ensuring the balance never goes beowzero#

class bankaccount:
    def __init__(self ,balance):
        self.__balance=balance

    def get_balace(self):
        return self.__balance
    def set_balace(self,updatebalance):
        if  0 < updatebalance:
            self.__balance=updatebalance
        else:
            print("invaled balence")
pgb=bankaccount(356)

print(pgb.get_balace())

pgb.set_balace(6578)
print(pgb.get_balace())

pgb.set_balace(-678)
print(pgb.get_balace())