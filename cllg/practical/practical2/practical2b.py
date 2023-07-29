def count(s):
    len=0
    for c in s:
        len +=1
    return len
str= input("Enter a String:")
print("\nLength of the String=",count(str))
print("\nLength=",count(list(str)))
l1= [10,20,30]
print("\n Length of the List=",count(l1))