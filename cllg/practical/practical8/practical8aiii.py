class Student:
    def division(self,name,rno):
        if rno <=80:
            div = "A"
        else:
            div = "B"
        print("{} is in Division {}".format(name,div))

s1 = Student()

s1.division("om",98)

print("-----------")

n =input("Enter your name:")
r= int(input("Enter your roll no:"))


s2=Student()
s2.division(n,r)
