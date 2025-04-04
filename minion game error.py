#it is game

def minion_game(string):
    k=0
    p2=0
    st=len(string)
    for i in range(st):
        if s[i] in "AEIOU":
            k += st- i
        else:
            p2 +=st-i
if  k>p2:
    print(f"1{p1}")
elif p2>k:
  print(f"2{p2}")
else:
    print(draw)

s=str(input("enter a string>>"))
