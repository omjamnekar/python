f= open("myfile.py","a+")

f.write("\n File Handling")
f.seek(0)

print(f.read())


f.close()