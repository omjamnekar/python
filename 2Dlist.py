matrix  =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
# matrix[0][1] = 20
# print(matrix[0][1])

for row in matrix:
    t = [0,0,0]
    for item in row:
        t += item
    print(t)