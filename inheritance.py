
class mix:
    def run(self):
        print('run')

class Dog:
    def walk(self):
        print('walk')

class Cat(Dog,mix):
        pass
dg =  Cat()
dg.walk()
dg.run()