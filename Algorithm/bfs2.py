from collections import deque

# 방향 정보 리스트 [상, 하, 좌, 우]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

t = int(input())


def bfs(graph, r, c):               # 파라미터로 2차원 리스트(graph), 행(r), 열(c) 받음
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

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))
    return


for _ in range(t):
    result = 0
    n, m, k = map(int, input().split())

    # 인접 행렬 - 모든 정보 저장
    # graph = [[0] * 열 for _ in range(행)]
    graph = [[0] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(graph, i, j)
                result += 1
    print(result)
