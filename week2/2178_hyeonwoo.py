N, M = map(int, input().split())

maze = []
for i in range(N):
    maze.append(input())

goal = [N-1, M-1]
min_depth = float('inf')

def can_go(x, y):
    directions = [(x+1, y), (x, y+1), (x-1, y), (x, y-1), ]
    next_poses = [
        [nx, ny]
        for nx, ny in directions
        if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == '1'
    ]

    return next_poses

def dfs(pos, depth, visited):
    global min_depth
    if pos == goal:
        if depth < min_depth: 
            min_depth = depth
        return 

    next_poses = can_go(pos)

    for next_pos in next_poses:
        if next_pos not in visited: 
            # print(next_pos)
            visited.append(pos)
            # copy를 안 하면 완전탐색을 못한다. But 시간초과 문제
            dfs(next_pos, depth+1, visited.copy())

depth_map = [[float('inf') for _ in range(M)] for _ in range(N)]

def bfs(pos):
    depth_map[pos[0]][pos[1]] = 1
    queue = [pos]

    while queue: 
        x, y = queue.pop(0)
        next_poses = can_go(x, y) 

        for nx, ny in next_poses:
            if depth_map[nx][ny] > depth_map[x][y]+1: 
                depth_map[nx][ny] = depth_map[x][y]+1
                queue.append([nx, ny]) 
    
    print(depth_map[N-1][M-1])

bfs([0, 0])
