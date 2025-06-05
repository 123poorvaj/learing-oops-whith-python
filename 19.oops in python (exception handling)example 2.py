#2. safe divider
# *Ask two number from the user and divide them.
# * handel zerodivision error and value error


try:
    n=int(input("enter your first number>>"))
    m=int(input("enter your second number>>"))
    div=n/m
    print(f" {n} /{m} = {div}")
except ZeroDivisionError:
    print("second number not equal to zero")
except ValueError:
    print("enter only integer number not string ")
