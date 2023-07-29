n= int(input("enter a number:"))
a,b,s =0,1,0
print(a,b,end="")
for x in range(n-2):
    s=a+b
    a,b =b,s
    print(s ,end=" ")

# 12

n3= int(input("enter a number:"))
a,b,s =0,1,0
x=1
print(a,b,end="")
while x<=(n3-2):
    s=a+b
    a,b=b,s
    x+=1
    print(s ,end=" ")