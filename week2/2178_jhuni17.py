# (1, 1) 에서 시작, (N, M)으로 도착 최소 칸 개수 구하기 -> (0, 0) 시작 (N-1, M-1) 도착
# 맵을 리스트로 저장
# 방문 리스트 초기화, 움직일 수 있는 경우 리스트 생성
# 이동할 수 있는지 확인하는 함수 생성
# queue 초기화, 처음 시작 위치와 거리 추가
# queue를 pop하고 이동할 수 있는 모든 지점 추가, 방문 처리, queue가 비어있을 때 까지 반복
# 목표 위치 도달 시 거리 저장 후 최소 거리 출력

N, M = map(int, input().split())
map = []

for i in range(N):
    row = input()
    r = []
    for j in row:
        r.append(int(j))
    map.append(r)
        
def solution(N, M, map):
    visit = [[0]*M for _ in range(N)]
    move = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    def can_move(x, y):
        return 0<=x<N and 0<=y<M and map[x][y]==1 and visit[x][y]==0
    
    queue = []
    distances = []
    x, y, dist = 0, 0, 1
    queue.append((x, y, dist))

    while queue:
        x, y, dist = queue.pop(0)
        for dx, dy in move:
            if can_move(x+dx, y+dy):
                queue.append((x+dx, y+dy, dist+1))
                visit[x+dx][y+dy] = 1 # 처음에 시간초과 였으나 방문처리 코드 위치 이곳으로 바꾸니 해결
                if (x+dx, y+dy) == (N-1, M-1):
                    distances.append(dist+1)

    return min(distances)

print(solution(N, M, map))