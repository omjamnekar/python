# NAME = ['john','BOD','mosh','sarah','Mary']
# print(NAME[1:3])
# print(NAME[0])
# print(NAME[-1])
# print(NAME)
# print(NAME[1:])
# NAME[0]= 'JON'
# print(NAME)


# number = [2,6,3,8,2,9,5,4,13]
# max = number[0]
# for i in number:
#    if i > max:
#       max = i
# print(max)
#

number = [2,5,4,5,5,6,7,3]
# number.append(13) # at last
# number.insert(0,10) # at 0 index insert 10
# number.remove(5) # remove the particular element
#
# # number.clear() clear all the element
# number.pop() # remove last element
# print(number.index(2)) # return type
# print(number)
# print(50 in number) # it  will give false output
# print(number.count(5))
# number.sort()   # sorting the list
# print(number)
#
# number.reverse()
# print(number)
# number2= number.copy()
# number.append(32)
# print(number2)
# print(number)


unique = []
for numbers in number:
    if numbers not in unique:
        unique.append(numbers)
print(unique)