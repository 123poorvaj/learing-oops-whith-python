#islower() : it return 'True' is all latter are lower case in the  string atherwise False. 
print('----------------islower()---------------')
string1='poorvaj' 
string2='Poorvaj'
print(f" '{string1}' is : {string1.islower()} and '{string2}' is :{string2.islower()}")
print("")
#isupper() :it return 'True' is all latter are upper case in the  string athorwise False. 

print('----------------isupper()---------------')
string1='POORVAJ' 
string2='P00rvaj'
print(f" '{string1}' is : {string1.isupper()} and '{string2}' is :{string2.isupper()}")
print("")
#isspace(): Returns True if the string contains only spaces, tabs (\t), or newlines(\n).

print('----------------isspace()---------------')
string1=' ' 
string2=' Poorvaj '
string3='\n\t'
print(f" 'space' is : {string1.isspace()} , '{string2}' is :{string2.isspace()} and tab,newline is : {string3.isspace()} ")
print("")
#iscasefold() :Converts a string to lowercase more aggressively than lower(). Useful for case-insensitive comparisons.
print('----------------iscasefold()---------------')
string1='POORVAJ' 
string2='POOrvaj'
print(f" {string1} and {string2} is same:{string1.casefold()== string2.casefold()}")
print("")
#swapcase():  Converts uppercase to lowercase and lowercase to uppercase.
print('----------------isswapcase()---------------')
string1='pooRvaJ'
print(f"{string1} After swapcase : {string1.swapcase()}")
print("")