# 1. age verifier
# * ask the user for thire age
# if age is valied (number),
# show in how may years they will be 100 year old .
# handel invalide input gracefully


try:
    n = int(input("enter your age >> "))
    year = 100 - n
    print(f"{year} years is remaining you be 100 year old")
except ValueError:
    print("enter only integer number")


