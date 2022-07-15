from collections import deque

# 상하좌우 방향 정보
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(graph, r, c):
    q = deque()                                 # 큐 생성
    q.append((r, c))                            # 시작 노드 큐에 삽입
    graph[r][c] = 1                             # 시작 노드 방문 처리

    area = 1                                    # 넓이 초기값 1

    # 큐가 빌 때까지 즉, 모두 방문 처리될 때까지 반복
    while q:
        x, y = q.popleft()                      # 큐에서 가장 첫번째 노드 꺼냄

        for i in range(4):                      # 상하좌우에 인접한 노드 확인
            nx = x + dx[i]
            ny = y + dy[i]

            # 직사각형을 벗어나는 경우 continue
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            # 인접한 노드가 방문되지 않은 경우
            if graph[nx][ny] == 0:
                graph[nx][ny] = 1               # 방문 처리
                q.append((nx, ny))              # 인접 노드 큐에 삽입

                area += 1                       # 넓이값

    return area                                 # 넓이값 반환


num = 0                                         # 빈 영역 갯수
m, n, k = map(int, input().split())             # 세로길이, 가로길이, 채워질 영역의 갯수
graph = [[0] * n for _ in range(m)]
lst = []

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1


for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            lst.append(bfs(graph, i, j))        # bfs 함수에서 반환된 넓이값 lst 리스트에 추가
            num += 1                            # 빈 영역 갯수

print(num)
lst.sort()
for i in range(num):
    print(lst[i], end=' ')
