import random
sse=random.randint(1,3)
print(sse)
chanse=1
while(True):
    guessnum=int(input("guess the number>>"))
    if  guessnum==sse :
        print("congratulation you get write answer")
        break
    else:
        print("your fail ")
        chanse+=1
        if chanse<5:
            print("take one more chanse")
        else:
            print(f"you take {chanse-1} chanse")
            print("yor chanse is close")
            break
