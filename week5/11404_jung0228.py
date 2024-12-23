n = int(input())
m = int(input())

graph = [[float('inf') for i in range(n)] for _ in range(n)]

for i in range(n):
    graph[i][i] = 0  # 자기 자신으로 가는 거리는 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], c)


for k in range(n): 
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(n):
    for j in range(n): 
        if graph[i][j] == float('inf'):
            graph[i][j] = 0

for i in range(n):      
    print(*graph[i])
