c =input("enter a character:")
if(ord(c)>=65 and ord(c)<=90):
  print("Uppercase letter")
elif(ord(c)>=97 and ord(c)<=122):
  print("Lowercase letter")
elif(ord(c)>=97 and ord(c)<=122):
  print("Lowercase letter")
elif(ord(c)>=48 and ord(c)<=57):
  print("Digits")
else:
  print("special symbols")