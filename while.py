re = 1
while re <=3:
    result = int(input('guess:'))
    if(result == 9):
        print('win')
        break

    re = re + 1
    if re >= 4:
        print('sorry you failed')
