class Person():
    def __init__(self,name):
        self.name =name
    def getName(self):
        return self.name
    def isStudent(self):
        return False

class Student(Person):
    def isStudent(self): 
        return True

p= Person("om")
print(p.getName(),p.isStudent())

s= Student("jamnekar")
print(s.getName(),s.isStudent(),Person.isStudent("PQR"))

print(issubclass(Person,Student))
print(issubclass(Student,Person))
print(isinstance(p,Person))
print(isinstance(s,Person))
print(isinstance(s,Student))
print(isinstance(s,Student))
