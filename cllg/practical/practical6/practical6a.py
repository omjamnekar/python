f = open("myfile.txt","w")
f.write("Hello World")
f.close()

f=open("myfile.txt","a+")
print(f.read())

f.write("\n BSCIT")
f.close()


f =open("myfile.txt","r+")
t= (f.read(3))
print(t)
print("correct position =",f.tell())

print(f.read())

f.write("\n python programming")
print("-----------------------")

f.seek(0)
print(f.read())

f.close()