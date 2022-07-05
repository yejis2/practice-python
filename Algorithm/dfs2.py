import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input())
graph = [list(input()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

area_cnt1, area_cnt2 = 0, 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 인덱스 범위 안에 있으면서, 같은 색이면서, 방문 안한 경우, dfs 재귀 호출
        if (0 <= nx < n) and (0 <= ny < n) and graph[nx][ny] == graph[x][y] and not visited[nx][ny]:
            dfs(nx, ny)


# 적록색약이 아닌 경우
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            area_cnt1 += 1

# 적록색약인 경우
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            area_cnt2 += 1

# 최종 출력
print(area_cnt1, area_cnt2)
