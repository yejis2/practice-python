graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

# DFS에서 데이터 찾을 때
# '앞으로 찾아 가야 할 노드'
# '이미 방문한 노드'를 기준으로 함

# 큐
from collections import deque

def dfs(graph, start_node):
    visited = []
    need_visited = deque()
    need_visited.append(start_node)             # 시작 노드 지정

    while need_visited:                         # 아직 방문되지 않은 노드가 있을 경우
        node = need_visited.pop()               # 그 중에서 가장 마지막 데이터를 추출

        if node not in visited:                 # 해당 노드가 방문 리스트에 없다면
            visited.append(node)                # 방문 리스트에 추가
            need_visited.extend(graph[node])    # 인접 노드들을 방문 예정 리스트에 추가

    return visited

print(dfs(graph, 'A'))
