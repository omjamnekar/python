fname= input("Enter a  filename:")
m = input("Enter Mode:")
try:
    f= open(fname,m)
    f.write("\nPython Programming")
    f.seek(0)
    print(f.read())

except FileNotFoundError:
    print("file does not exist")
except IOError:
    print("Cannot read/write data")
except ValueError:
    print("Incorrect file mode")
else:
    f.close()