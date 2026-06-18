#find() : it use to find the position of the charecter or word 
print("--------------find()----------------")
text = 'poorvaj'
position=text.find('j')
position_of_aj=text.find('aj')
print(f'position of  j >{position} position of word aj >> {position_of_aj}')
print("")
print("--------------split()--------------")
#split() : it use to convert string into list,separate the string using space
text='hello poorvaj M Gowda'
print("After split the string >> ",text.split())
print("")
print("---------------join()---------------")
#join (): it use to join the list of string into one string 
#syntax for join method : separater.join(list)

list_of_words=text.split()
separater='_' #separater take any string value 
print("After joining the string > ",separater.join(list_of_words))
print("")
print("----------------isalpha()-------------")
#isalpha(): use to check if all charecter are latters or not 
#is the string contains only laters retrun 'True' otherwise return 'False' 

word1='poorvaj'
word2='poorvaj123'
print(f"poorvaj is >> {word1.isalpha()} , poorvaj123 is >> {word2.isalpha()}")
print("")
print("-----------------isalnum()--------------")
#isalnum(): it's return True only if the string containes only latters or numbers. 
word3='123##pp'
print(f"poorvaj isalnum > {word1.isalnum()}, poorvaj123 isalnum > {word2.isalnum()} , 123##pp isalnum > {word3.isalnum()}")