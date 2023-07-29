def reverse(n):
    rev = 0
    while(n!=0):
        rem = n%100
        rev = (rev*10)+rem
        n //=10
    return rev

num = int(input("Enter a number:"))
print("Reverse of",num,"=",reverse(num))
