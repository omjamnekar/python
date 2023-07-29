class Student:
    college ="M.L.D.C"
    Class = "SY.B.S.c.(I.T)"
    def  __init__(self):
        self.name= "ABC"
        self.rno=1
    def division(self):
        if self.rno <80:
            self.div="A"
        else:
            self.div = "B"
        print("{} is in Division {}".format(self.name,self.div))

print(Student.college)
s1= Student()
print(s1.Class)

s1.division()

print("______________")
s2= Student()
s2.name= "Om"
s2.rno = 98
s2.division()
print("_______________")
s3 =Student()
n =input("Enter your name:")
r = int(input("Enter your roll no:"))

s3.name=n
s3.rno=r
s3.division()