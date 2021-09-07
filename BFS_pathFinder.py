from collections import deque
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동방향 up, down, left, right
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    q = deque()
    q.append((x,y))

    while q:
        x,y  = q.popleft()
        # 4방 확인
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny<0 or nx >=n or ny >=m or graph[nx][ny]==0:
                continue
            if graph[nx][ny] ==1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))
    return graph[n-1][m-1]

print(bfs(0,0))