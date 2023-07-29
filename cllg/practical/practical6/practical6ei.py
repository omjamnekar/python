f=open("abc.txt","r")

lines =len(f.readlines()) #5
n = int(input("Enter no. of lines for read from the end:"))#2
diff= lines-n #5-2  3
f.seek(0)
for line in f.readlines()[diff:]:
    print(line)
f.close()