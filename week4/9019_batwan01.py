from collections import deque

def dslr(start, target):
    visited = [False] * 10000
    queue = deque([(start, "")])
    
    while queue:
        current, commands = queue.popleft()
        
        if current == target:
            return commands
        
        D = (2 * current) % 10000
        if not visited[D]:
            visited[D] = True
            queue.append((D, commands + "D"))
        
        S = 9999 if current == 0 else current - 1
        if not visited[S]:
            visited[S] = True
            queue.append((S, commands + "S"))
        
        L = (current % 1000) * 10 + current // 1000
        if not visited[L]:
            visited[L] = True
            queue.append((L, commands + "L"))
        
        R = (current % 10) * 1000 + current // 10
        if not visited[R]:
            visited[R] = True
            queue.append((R, commands + "R"))

N = int(input())
for _ in range(N):
    n1, n2 = map(int, input().split())
    print(dslr(n1, n2))
