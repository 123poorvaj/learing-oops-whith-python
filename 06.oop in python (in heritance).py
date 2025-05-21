class user:
    def  __init__(self, username):
        self.username=username
    def login(self):
        print(f"{self.username} is  login")
class adm(user):
    def delet_user(self,usern):
        self.usern=usern
        print(f"{self.username } delet this {self.usern}   ")
adim=adm("poorvaj")
user=user("kumar")
print(f"name of the admine is {adim.username}\t")
print(f"name of the user is {user.username}")
adim.login()
user.login()
adim.delet_user(user.username)


