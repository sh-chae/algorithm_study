# row = n, col = m
n, m = map(int, input().split())
ans = []
for row in range(n):
    ans.append(min(map(int, input().split())))
print(max(ans))