'''
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
'''

from collections import deque

def add_graph(graph, F, S):
    graph[F].append(S)
    graph[S].append(F)
    return graph

def bfs(graph, start):
    visited = set()
    que = deque([start])
    visited.add(start)

    result = []
    while que:
        node = que.popleft()
        result.append(node)

        for num in sorted(graph[node]):
            if num not in visited:
                que.append(num)
                visited.add(num)
    print(" ".join(map(str, result)))

def dfs(graph, node, visited):
    visited.add(node)
    print(node, end = " ")
    for num in sorted(graph[node]):
        if num not in visited:
            dfs(graph, num, visited)


N, M, V = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = set()

for _ in range(M):
    F, S = map(int, input().split())
    graph = add_graph(graph, F,S)

dfs(graph, V, visited)
print()
bfs(graph, V)