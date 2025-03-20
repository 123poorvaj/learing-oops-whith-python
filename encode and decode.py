import base64
message=input("entre your secret massege>>")
def encoded():
    massege_in_bytes=bytes(message,"utf-8")
    encoded_message=base64.b64encode(massege_in_bytes)
    print(encoded_message)
def decoded():
    massege_in_bytes = bytes(message, "utf-8")
    decoded_message = base64.b64decode(massege_in_bytes)
    print(decoded_message)

print("both encoder and decoder is available")
print("1,encoded and 2, decoded ")
option=int(input("select option 1/2>> "))
if option==1:
    encoded()
elif option==2:
    decoded()
else:
    print("your option is roung. try again")