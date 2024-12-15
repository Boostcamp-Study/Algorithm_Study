# 11403 경로 찾기

from collections import defaultdict

N = int(input())

adj_dict = defaultdict(list)
for i in range(N):
    node_arr = map(int, input().split())
    for idx, node in enumerate(node_arr):
        if node == 1:
            adj_dict[i].append(idx)

def solution(adj_dict, N):
    for i in range(N):
        queue = []
        visit = set()
        queue.append(i)
        while queue:
            node = queue.pop(0)
            for neighbor in adj_dict.get(node, []):
                if not neighbor in visit:
                    visit.add(neighbor)
                    queue.append(neighbor)
        
        for idx in range(N):
            if idx in visit:
                print(1, end=' ')
            else:
                print(0, end=' ')
        print()

solution(adj_dict, N)

        
