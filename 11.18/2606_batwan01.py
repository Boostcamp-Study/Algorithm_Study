def dfs(g, v, visited):
    visited[v] = True
    for i in g[v]:
        if not visited[i]:
            dfs(g,i,visited)
            graph[0]+=1

def insert_graph(graph, v, n):
    graph[v].append(n)
    graph[n].append(v)

num = int(input())
N = int(input())

graph = [[] for _ in range(num+1)]
visited = [False] * (num + 1)
graph[0] = 0

for _ in range(N):
    v, n = map(int, input().split())
    insert_graph(graph, v, n)

dfs(graph, 1, visited)
print(graph[0])