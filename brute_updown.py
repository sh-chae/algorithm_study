n = int(input())
dir = input().split()

start = [1, 1]

for dd in dir:
    if dd == "L" and start[1]!=1:
        start[1] -= 1
    if dd == "R" and start[1]!=n:
        start[1] += 1
    if dd == "U" and start[0]!=1:
        start[0] -= 1
    if dd == "D" and start[0]!=n:
        start[0] += 1    
print(*start)
