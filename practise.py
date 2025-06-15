def balnce(func):
    def warpwr():
        print("first balance ")
        func()
        print("third balance")
    return warpwr

@balnce

def tt():
    print("second balance")

tt()