# 2606 바이러스
# 딕서녀리로 연결 컴퓨터 표현
# 연결 컴퓨터를 1부터 bfs로 탐색, 집합에 방문 컴퓨터 기록

cpu_num = int(input())
N = int(input())

connect = {}
for _ in range(N):
    a, b = map(int, input().split())
    if a not in connect:
        connect[a] = [b]
    else:
        connect[a].append(b)
    if b not in connect:
        connect[b] = [a]
    else:
        connect[b].append(a)

def solution(connect):
    visit = set()
    queue = []
    queue.append(1)
    while queue:
        cpu = queue.pop(0)
        visit.add(cpu)
        if cpu in connect:
            for node in connect[cpu]:
                if node not in visit:
                    queue.append(node)
    
    return len(visit) - 1

if N == 0:
    print(0)
else:
    print(solution(connect))