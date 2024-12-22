# 7576 토마토

from collections import deque

M, N = map(int, input().split())

warehouse = []

for _ in range(N):
    warehouse.append(list(map(int, input().split())))

def solution(M, N, warehouse):
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def can_move(x, y):
        if 0<=x<N and 0<=y<M and warehouse[x][y] == 0:
            return True

    queue = deque()
    for i in range(N):
        for j in range(M):
            if warehouse[i][j] == 1:
                queue.append((i, j, 0))
    
    while queue:
        x, y, day = queue.popleft()
        for dx, dy in move:
            if can_move(x+dx, y+dy):
                warehouse[x+dx][y+dy] = 1
                queue.append((x+dx, y+dy, day+1))
    
    for i in range(N):
        for j in range(M):
            if warehouse[i][j] == 0:
                return -1

    return day

print(solution(M, N, warehouse))