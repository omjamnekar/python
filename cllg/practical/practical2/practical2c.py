def histogram(n):
    for i in n:
        print("*"*i)
r= int(input("Enter no of rows in histogram: "))
num=[]

for i in range(r):
    num.append(int(input("Enter value for rows:".format(i+1))))
histogram(num)