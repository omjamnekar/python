sub={"s1":"pp","s2":"DS","s3":"CN","s4":"OS","s5":"AM/MP"}
print(sorted(sub.values()))
print(sorted(sub.values(),reverse=True))


temp ={}
for k,v in sub.items():
    temp.update({v:k})

print("\n Dictionary in ascending order of values:")
for k,v in sorted(temp.items()):
    print("{}:{}".format(v,k))


print("\n Dictonary in descending order of values:")
for k,v in sorted(temp.items(),reverse=True):
    print("{}:{}".format(v,k))
