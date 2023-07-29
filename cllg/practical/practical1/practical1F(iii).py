def armstrong(n):
    s=0
    temp=n
    p = len(str(n))
    while(temp!=0):
        digit =temp%10
        s +=digit**p
        temp //=10
    
    if(s==n):
        print(n,"it is Armstrong Number")
    
    else:
        print(n,"is not an Armstrong Number")


num= int(input("enter a number:"))
armstrong(num)
