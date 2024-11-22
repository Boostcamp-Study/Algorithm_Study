# 1260 DFS와 BFS 

# 문제 설명
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 
# 정점 번호는 1번부터 N번까지이다. 

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

# 그래프 만들기
for _ in range(M): 
  a, b = map(int, input().split())
  graph[a].append(b) 
  graph[b].append(a)
  
for i in range(N+1):
  graph[i].sort()

# bfs 함수 정의
def dfs(i, path):
  visited[i] = True 
  path.append(i)
  
  for neighbor in graph[i]:
    if not visited[neighbor]:
      dfs(neighbor, path)
  
  return path

def bfs(start, path):
  queue = [start] 
  path.append(start) 
  visited[start] = True 
  
  while queue: 
    q = queue.pop(0) 
    for neighbor in graph[q]: 
      if not visited[neighbor]:
        queue.append(neighbor)
        path.append(neighbor) 
        visited[neighbor] = True
  
  return path
     
visited = [False for _ in range(N+1)]
dfs_result = dfs(V, [])
print(*dfs_result)  # 리스트를 공백으로 구분하여 출력

visited = [False for _ in range(N+1)]
bfs_result = bfs(V, [])
print(*bfs_result) 