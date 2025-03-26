#textwarp is used to warp AND formate planing text.
#syntax (textwarp.fill(varible,width)
import textwrap
def warp():
    print(textwrap.fill(me,length))
def validators():
    print(me.lower())

me=input("enter the massege>>")
length=int(input("enter the string width>> "))
if length==4:
    warp()
elif length==2:
    validators()
else:
    print("your option is wroung")


