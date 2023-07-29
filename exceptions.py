try:
    age = int(input('age:'))
    income = 20000
    risk = income /age
    print(age)
except ValueError:
    print('Invalid error')
except ZeroDivisionError:
    print('age cannot be 0')
