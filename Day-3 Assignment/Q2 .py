keys=[]
values=[]
l=int(input("Enter the dictonary length : "))
for i in range(l):
    keys.append(int(input("Enter the key : ")))
    values.append(input("Enter the Value : "))
dictonary=dict.fromkeys(keys,0)
for i in range(l):
    dictonary[keys[i]]=values[i]
print("key's     : ",keys)
print("value's   : ",values)
print("dictonary : ",dictonary)
