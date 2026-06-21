#uppercase later pyramid patteren 
#input : 5 
'''
    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDCBA
'''
#input : 3
''' 
   A
  ABA
 ABCBA
'''
#the pattren should be center-align with largest row having 2*n+1 charecter
# code:

n=int(input("Enter the number of row : "))

for i in range(0,n):
    k=0
    space=n-i-1
    print(" "*space,end="")
    for j in range(0,(2*i+1)):
        print(chr(ord('A')+k),end="")
        if i<=j:
            k-=1
        else:
            k+=1
    print("")
