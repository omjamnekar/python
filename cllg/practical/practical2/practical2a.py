def vowel(c):
    return (c.lower() in ['a','e','i','u','o'])
c=input("Enter a character:")
if vowel(c):
    print("vowel")
else:
    print("Comsonant")