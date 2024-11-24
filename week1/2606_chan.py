import sys
from collections import deque

# bfs
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 입력
num_com = int(sys.stdin.readline().rstrip())
num_connect = int(sys.stdin.readline().rstrip())
connect = [list(map(int, sys.stdin.readline().split())) for _ in range(num_connect)]

# visited list 및 graph 구조로 변환
visited = [False] * (num_com +1)
graph = [[] for _ in range(num_com + 1)]

for con in connect:
    graph[con[0]].append(con[1])
    graph[con[1]].append(con[0])

# bfs로 1과 연결된 node 찾기
bfs(graph, 1, visited)

# 출력
sys.stdout.write(str(sum(visited)-1))