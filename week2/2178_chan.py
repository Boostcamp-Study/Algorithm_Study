import sys
from collections import deque

# NxM = 10000 <= 100,000 : O(NlogN) **

# 입력
N, M = map(int, sys.stdin.readline().split())

# graph 변환
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

# 이동방향 정의 (상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            # 이동 불가 무시
            if new_x < 0 or new_y < 0 or new_x > (N-1) or new_y > (M-1):
                continue
            if graph[new_x][new_y] == 0:
                continue
            if graph[new_x][new_y] == 1:
                graph[new_x][new_y] = graph[x][y] + 1
                queue.append((new_x, new_y))
    
    return graph[N-1][M-1]

sys.stdout.write(str(bfs(0, 0)))

