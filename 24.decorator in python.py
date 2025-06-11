
def deeg(func):
    def wrappe(a,b):
        print(f" {func.__name__} ",end="")
        func(a,b)
    return wrappe



@deeg
def sub(a,b):
    print(a-b)
    


@deeg
def add(a,b):
    print(a+b)

add(23,45)
sub(45 ,67)
