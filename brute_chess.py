start = input()
start = [int(start[1]), ord(start[0])-96]

count = 0
direc = [[2, 1], [2, -1], [-2, 1], [-2, -1],
         [1, 2], [1, -2], [-1, 2], [-1, -2]]
for i in direc:
    if 0<i[0]+start[0] <= 8 and 0<i[1]+start[1] <= 8:
        count += 1

print(count)
