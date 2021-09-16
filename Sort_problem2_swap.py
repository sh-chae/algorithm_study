n,k = map(int, input().split())
a_array = map(int, input().split())
b_array = map(int, input().split())

# n = 5
# k = 3
# a_array = [1, 2, 5, 4, 3]
# b_array = [5, 5, 6, 6, 5]

a_array.sort()
b_array.sort(reverse=True)
for i in range(k):
    if a_array[i] < b_array[i]:
        a_array[i], b_array[i] = b_array[i], a_array[i]
    else:
        break

print(sum(a_array))
