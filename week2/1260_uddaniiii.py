from collections import deque

# DFS 함수 정의
def dfs(graph, visited, node):
    visited[node] = True  # 현재 노드 방문 처리
    print(node, end=" ")  # 방문한 노드 출력
    for neighbor in graph[node]:
        if not visited[neighbor]:  # 아직 방문하지 않은 노드라면
            dfs(graph, visited, neighbor)  # 재귀적으로 DFS 호출

# BFS 함수 정의
def bfs(graph, visited, start):
    queue = deque([start])  # 큐에 시작 노드를 넣는다.
    visited[start] = True  # 시작 노드를 방문 처리
    
    while queue:
        node = queue.popleft()  # 큐에서 노드를 꺼낸다.
        print(node, end=" ")  # 현재 노드를 출력
        for neighbor in graph[node]:
            if not visited[neighbor]:  # 아직 방문하지 않은 노드라면
                visited[neighbor] = True  # 방문 처리
                queue.append(neighbor)  # 큐에 인접 노드를 추가

# 그래프 입력 처리
n, m, start = map(int, input().split())  # 노드 수, 간선 수, 시작 노드
graph = {i: [] for i in range(1, n + 1)}  # 빈 인접 리스트 초기화

# 간선 정보 입력 받아서 그래프 구성
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  # 양방향 연결

# 각 노드의 인접 노드를 오름차순으로 정렬 (작은 번호부터 탐색)
for node in graph:
    graph[node].sort()

# DFS 탐색
visited = [False] * (n + 1)  # 방문 여부 초기화
dfs(graph, visited, start)  # DFS 호출
print()  # 줄 바꿈

# BFS 탐색
visited = [False] * (n + 1)  # 방문 여부 초기화
bfs(graph, visited, start)  # BFS 호출
