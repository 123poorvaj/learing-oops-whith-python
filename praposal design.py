length=8
width=20
for i in range(1,length,2):
    print(('~'*i).center(width,' '))

print('I love you'.center(width,' '))
for i in range(length-1,-1,-2):
    print(('~'*i).center(width, ' '))