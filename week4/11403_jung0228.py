n = int(input()) 

graph = [list(map(int, input().split())) for _ in range(n)]

# print(graph)

for i in range(n):
    for j in range(n):
        for k in range(n):
            if graph[j][i] == 1 and graph[i][k] == 1:
                graph[j][k] = 1

for i in range(n):
    print(*graph[i])