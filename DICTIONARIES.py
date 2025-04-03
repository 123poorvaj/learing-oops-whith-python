#dictionaries containce key and value.
#it ise used to list of elements with value.
#syntax ={"key":value} and print(variable[key])
# for example:
m={"pen": 20,"book":50,"bag":400,"lunch box":200}
print(m["pen"]) # o/p: 20

# access and madify elements in a dictionrary
print(m.values()) #value is use to print only value
print(m.keys()) #keys is use to print only keys

m.pop("bag")# pop is use to remove the elements
print(m)

m.update({"bag":400})#update is use to insert the new one
print(m)

