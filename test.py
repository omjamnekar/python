# weight = int(input('Weight'))
# k_p = input('(L)bs or (K)g:')
# kg = k_p.upper()
# if (kg == 'K'):
#     result  = weight/ (0.45)
#     print(f'you are {result} pounds')
# else:
#     result = weight * (0.45)
#     print(f'you are {result} kg')
#

# result = input('>').lower()
# i = 1
# c= 1
# d = 1
# e = 1
# while i ==1:
#  if (result == 'help'):
#
#        print("""
#        start - to start the car
#        stop - stop the car')
#        quit - to exit
#        """)
#        while i == 1 :
#           result2 = input('>').lower()
#           if result2 == 'start' or result2 == 'stop' or result2 == 'quit':
#
#              if result2 == 'start' and c < 1:
#                   print('car is start',c)
#                   c = c + 2
#              if result2 == 'start' and c ==1:
#                  print('car is start',c)
#                  c = c+1
#              elif result2 == 'stop' and e <= 1:
#                  print('car is stop', e)
#                  e = e + 2
#                  c = c - 1
#              elif result2 == 'stop' and e ==1:
#                  print('car is stop',e)
#                  e = e+1
#                  c = c -1
#              elif result2 == 'quit' and d==1:
#                  print('exit')
#                  i = i+1
#                  d= d+1
#                  break
#
#              elif result2 == 'start' and c >= 2:
#                  print('already started',c)
#                  e = e-1
#                  c = c +1
#              elif result2 == 'stop' and e == 2:
#                  print('already stop',c)
#
#              elif result2 == 'quit' and d == 2:
#                  print('exit')
#                  i = i + 1
#                  break
#           else:
#             print("I don't understand that...")
#
#  elif result == 'stop' and c==1:
#     print('car is already stop')
#     result = 'stop'
#  elif result == 'start' and c==1:
#      print('car is started')
#      c =c +1
#  elif result == 'quit' and c==1 :
#      print('quit')
#      i= i+1
#      break
#
#  elif result == 'stop' and c==2:
#     print('car is already stop')
#     result = 'stop'
#  elif result == 'start' and c==2:
#      print('car is already started')
#  elif result == 'quit' and c==2 :
#      print('quit')


# price = [10,20,30]
# result = 0
# for item in price:
#     result = result +item
# print(result)


#module
import module_container

# from module_container import find_max
#
# numbers = [10,23,1,32]
# find_max(numbers)