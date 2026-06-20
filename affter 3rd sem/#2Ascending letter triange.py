#Ascending Uppercase Latter Triangle 

# input : n=6 
'''output: 
A
A B 
A B C
A B C D E
A B C D E F 

'''
#topics ,loops ,ascii value converstion

n=int(input("Enter the number of rows>> "))
for i in range(0,n):
    for j in range(0,i+1):
        print(chr(ord('A')+j),end=' ')
    print('')

