dictionary={"bike":1,"bus":2,"cab":3,"taxi":4,"auto":5}
print("KEYS")
print()
for key in dictionary.keys():
    print(key)
print("VAlUES")
print()
for values in dictionary.values():
    print(values)

    
remove=dictionary.popitem()
print(remove)
print(dictionary)
dictionary["car"]="tesla"
print(dictionary)
convert=list(dictionary.items())
print(convert)