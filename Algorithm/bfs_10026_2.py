

from collections import deque

n = int(input())
graph = [list(input()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

area_cnt1, area_cnt2 = 0, 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    visited[x][y] = 1

    while q:
        x, y = q.popleft()

        # 방향 정보
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 인덱스 범위 안에 있으면서, 같은 색이면서, 방문 안한 경우
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == graph[x][y] and not visited[nx][ny]:
                visited[nx][ny] = 1  # 방문체크 후 큐에 넣음
                q.append((nx, ny))


# 적록색약이 아닌 경우
for i in range(n):
    for j in range(n):
        if not visited[i][j]:  # 아직 방문 안한 경우만 체킹
            bfs(i, j)
            area_cnt1 += 1

# 적록색약인 경우
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'


for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            area_cnt2 += 1

# 최종 출력
print(area_cnt1, area_cnt2)
