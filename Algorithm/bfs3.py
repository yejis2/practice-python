from collections import deque

# 방향 정보 리스트 [위, 아래, 왼, 오, 왼위, 왼아래, 오위, 오아래]
dx = [0, 0, 1, -1, -1, -1, 1, 1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]

def bfs(graph, r, c):               # 파라미터로 2차원 리스트(graph), 행(r), 열(c) 받음
    q = deque()
    q.append((r, c))
    graph[r][c] = 0

    while q:
        # 가장 첫번째 데이터 추출
        x, y = q.popleft()
        for i in range(8):
            # 현재 좌표 + 방향 정보
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))
    return


while True:
    result = 0
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    # 인접 행렬 - 모든 정보 저장
    # graph = [[0] * 열 for _ in range(행)]
    graph = []

    for i in range(h):
        graph.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(graph, i, j)
                result += 1
    print(result)
    del graph
