array = []
for i in range(int(input())):
    array.append(int(input()))

print(*sorted(array, reverse=True))