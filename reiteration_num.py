# 리스트의 항목을 총 m 번 더해서 가장 큰 수를 찾는다 다만 같은항목이 k번 이상 반복도리수 없다.
n,m,k = map(int, input().split())
ll = sorted(list(map(int, input().split())))

first = ll[-1]
second = ll[-2]
ans = (m%k)*second + (m-m%k)*first
print(ans)