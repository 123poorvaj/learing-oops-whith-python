#syntax of the decoraters
def decoratore_name(func):
    def wrappe():
        print("are you study")
        func()
    return wrappe


@decoratore_name
def student():
    print("yes i am study")


student()
