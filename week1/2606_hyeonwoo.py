# 2606번 문제
# 문제 링크: https://www.acmicpc.net/problem/2606

# 문제 설명
# 컴퓨터의 네트워크 상에서 연결된 컴퓨터의 쌍의 수를 구하는 문제

N = int(input())
M = int(input()) 

l = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split()) 
    l[a].append(b)
    l[b].append(a)

infected = [False for _ in range(N+1)]

def bfs(idx):
    queue = [idx]
    infected[idx] = True
    
    while queue:
        k = queue.pop(0)
        for neighbor in l[k]:
            if not infected[neighbor]:
                infected[neighbor] = True 
                queue.append(neighbor) 
    
            
bfs(1)
print(sum(infected)-1) 
    