from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(graph, r, c):
    q = deque()
    q.append((r, c))
    graph[r][c] = 0

    rst = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))

                rst += 1

    return rst


num = 0
n = int(input())
graph = []
lst = []

for i in range(n):
    graph.append(list(map(int, input())))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            lst.append(bfs(graph, i, j))
            num += 1

print(num)
lst.sort()
for i in range(num):
    print(lst[i])
