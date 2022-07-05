import copy
from collections import deque

# 방향 정보 리스트 [상, 하, 좌, 우]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(graph, r, c, col):               # 파라미터로 2차원 리스트(graph), 행(r), 열(c), color 받음
    q = deque()
    q.append((r, c))
    graph[r][c] = 0

    while q:
        # 가장 첫번째 데이터 추출
        x, y = q.popleft()
        for i in range(4):
            # 현재 좌표 + 방향 정보
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == col:
                # 방문표시
                graph[nx][ny] = 0
                # 큐에 넣기
                q.append((nx, ny))
    return


result = 0
result2 = 0

n = int(input())

graph = []

for i in range(n):
    graph.append(list(input()))

graph2 = copy.deepcopy(graph)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            bfs(graph, i, j, 'R')
            result += 1
        if graph[i][j] == 'G':
            bfs(graph, i, j, 'G')
            result += 1
        if graph[i][j] == 'B':
            bfs(graph, i, j, 'B')
            result += 1

for i in range(n):
    for j in range(n):
        if graph2[i][j] == 'R':
            graph2[i][j] = 'G'

for i in range(n):
    for j in range(n):
        if graph2[i][j] == 'G':
            bfs(graph2, i, j, 'G')
            result2 += 1
        if graph2[i][j] == 'B':
            bfs(graph2, i, j, 'B')
            result2 += 1

print(result, result2)
