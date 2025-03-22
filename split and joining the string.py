

def spliting_the_string():
    print(a.split())
# this code is complitly based on the spliting the sring into list of the string.
#a="the king standing on the "
#syntax of spliting the string is  (a.split()).

def list_joining():
    print("-".join(b))
# this code is use to joing the list of sting .
# syntax is ("joing space".join(variable))

a="I am a student"
b=["I","am","a","student"]
print("option >>1.spliting and 2.list joining")
option=int(input())
if option==1:
   spliting_the_string()
elif option==2:
    list_joining()
else:
    print("your option is wrong ")    

