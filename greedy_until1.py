# step : n-1 or n /= k if n%k==0
# minimize steps
n, k = map(int, input().split())

steps = 0
while n!=1:
    if n%k ==0:
        n/=k
    else: n-=1

    steps += 1
print(steps)