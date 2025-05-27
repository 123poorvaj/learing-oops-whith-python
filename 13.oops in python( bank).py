class account:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        self._balence=0
    def chech_balence(self):
        print(" your balence is :",self._balence)

    def deposite(self,amount):
        self._balence+=amount
        print("your amount is succuess fully deposite\nupdated balence : ",self._balence)
    def withdraw(self,amount):
        if amount>self._balence:
            print("your account is not have this much amount")
        elif amount<=self._balence:
            self._balence-=amount
            print("withdrow succesfuly\nremaining balence : ",self._balence)




class savings_account(account):
        def addintrest(self):
            self.intrest=0.05
            self._balence=self._balence*self.interst
            print("intrest>>",self.intrest)
            print(self._balence)

class current_account(account):
    def withdraw(self,amount):
        self.limit=2000
        if self._balence + self.limit >=amount:
            self._balence-=amount
            print("withdrow succesfuly \n remaining balence : ", self._balence)
        elif self._balence + self.limit < amount:
             print("you ask more than limit amount")
        print(self._balence)


class bank:

      def __init__(self,name,city):
          self.name=name
          self.city=city
          self.__accounts={}
      def createaccuount(self,id,name,type):
          #type=input("enter your account type saving or current acount")
          if type=="savings":
              new_account=savings_account(id,name)
              print("your savings account created succesfully")
          elif type=="current":
              new_account=current_account(id,name)
              print("your current account created succesfully")
          self.__accounts[id]=new_account
          return new_account
      def get_account(self,id):

          if id not in self.__accounts:
              print("account not exist")
              return None
          else:
              account = self.__accounts[id]
              print(f"ID: {account.id}\nName: {account.name} \n ")

              return account

poo=bank("pkg","hb")
s1=poo.createaccuount(405,"sonu","savings")
p1=poo.createaccuount(356,"poorvaj","current")

s1.deposite(100)


p1.deposite(1000)
s1.withdraw(2000)


p1.withdraw(3000)


poo.get_account(356)
poo.get_account(405)