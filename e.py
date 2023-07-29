from pathlib import Path

path = Path("email")


# use for verifying does it exist
print(path.exists())

#use for creating new file,folder,exe,xlc,py
print(path.mkdir())

#use for deleting derectories

print(path.rmdir())

print(path.glob('*'))
#<generator object Path.glob at 0x0000015585521AD0>
print(path.glob('*.*'))
#<generator object Path.glob at 0x0000015585521AD0>
paths = Path()
for i in paths.glob('*.py'):
  print(i)
#app.py
# class.py
# constructor.py
# dictionary.py
# e.py
# exceptions.py
# for.py
# function.py
# if-else.py
# inheritance.py
# input.py
# LIST.py
# main.py
# module.py
# module_container.py
# nested.py
# random.py
# string.py
# test.py
# tuple.py
# unpacking.py
# while.py