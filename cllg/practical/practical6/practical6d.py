 

f1 = open("file1.txt", "r")
f2 = open("file2.txt", "r")
f_new = open("file3.txt", "w+")
f_new.write(f1.read())
f_new.write(f2.read())
f_new.seek(0, 0) 
print(f_new.read())

f1.close()
f2.close()
f_new.close()


# Hello world 
# have a nice day

# SYBSCIT
# Python programming