from collections import deque

M, N = map(int, input().split())
farm = []
queue = deque()
days = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    row = list(map(int, input().split()))
    farm.append(row)
    for j in range(M):
        if row[j] == 1:
            queue.append((i, j))

while queue:
    for _ in range(len(queue)):
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위 체크 및 익지 않은 토마토 확인
            if 0 <= nx < N and 0 <= ny < M and farm[nx][ny] == 0:
                farm[nx][ny] = 1
                queue.append((nx, ny))
    
    if queue:
        days += 1

# 모든 토마토가 익었는지 확인
for row in farm:
    if 0 in row:
        days = -1
        break

print(days)
  