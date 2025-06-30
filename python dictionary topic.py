#*dictionary.
#it is use to store the multiple items with key value paires.
#dictionary created using flower bracket .
#syntax is dictionary_name={key;value,key:value,,,,,,,,,}

a={ 1:"poorvaj",2:"sonu",3:"kisu",4:"adi"}
print(a)
#how to change the dictionary value
#synax is name[key]=resent value
a[2]="pooja"
print(a)

#how to print only one element
#syntax is print(name[key])
print(a[3])

#how to add new key and value
#syntax is name[new key]= new value
a[5]="new"
print(a)

#how to print only values
print(a.values())

#how to print only keys
print(a.keys())

#how to print hole dictionary items
print(a.items())



