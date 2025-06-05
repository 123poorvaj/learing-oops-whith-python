#file reader:
# *Ask the user for a file name and try to open it.
# * show error message if file doesn't exist
# *use finally to print "program is end "#

try:
    name=input("enter your file name")
    file=open(name,'r')
except FileNotFoundError:
    print("file not found")
finally:
    print("program is end")

