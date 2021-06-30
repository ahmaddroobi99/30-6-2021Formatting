s = 0
x = [[1, 2, 3, 4, 6, 5, 8, 9, 2], [1, 2, 3, 4, 6, 5, 8, 9, 2], [1, 2, 3, 4, 6, 5, 8, 9, 2]]
for i in range(len(x) - 1):
    for j in range(len(x) - 1):
        s = s + x[i][j]

print(s)



