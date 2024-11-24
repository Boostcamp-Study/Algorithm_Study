'''
N×M크기의 배열로 표현되는 미로가 있다.

1	0	1	1	1	1
1	0	1	0	1	0
1	0	1	0	1	1
1	1	1	0	1	1

미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.
'''
from collections import deque

def find_route(graph):
    rows, cols = len(graph), len(graph[0])
    destination = [(-1,0), (1,0), (0,-1), (0,1)]
    visited = [[False]*cols for _ in range(rows)]
    
    que = deque([(0,0,1)])
    visited[0][0] = True

    while que:
        x, y, step = que.popleft()
        
        if x == rows - 1 and y == cols -1:
            return step
        
        for dx, dy in destination:
            nx, ny = x+dx, y+dy
            if 0 <= nx < rows and 0 <= ny < cols and graph[nx][ny] == 1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                que.append([nx, ny, step+1])

    return -1

N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]

print(find_route(graph))