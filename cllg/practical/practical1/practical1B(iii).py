a= input("enter area code:")
s= int(input("enter sale:"))
if(a== "C"):
 if(s>=100000):
    c= s*0.10
 elif(s>=50000):
   c= s*0.05
 else:
   c=1000
 print("\n commision= ",c)
elif(a=="V"):
 if(s>=100000):
    c= s*0.15
 elif(s>=50000):
   c= s*0.08
 else:
   c=1500
 print("\n commision= ",c)
else:
  print("\n\n Invalid Area code")
