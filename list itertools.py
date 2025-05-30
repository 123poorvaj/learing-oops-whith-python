from itertools import product
a=map(int,input("a>>").split()) #[1,2]
b=map(int,input("b>").split()) #[3,4]

print(*product(a,b)) #[(1,3) (1,4) (2,3) (2,4)]