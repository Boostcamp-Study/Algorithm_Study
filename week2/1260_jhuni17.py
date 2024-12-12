# 1260 DFS와 BFS

from collections import defaultdict

N, M, V = map(int, input().split())

adj_list = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

visit_dfs = set()
result_dfs = []

def dfs(adj_list, node):
    visit_dfs.add(node)
    result_dfs.append(node)
    for neighbor in sorted(adj_list.get(node, [])):
        if neighbor not in visit_dfs:
            dfs(adj_list, neighbor)


def bfs(adj_list, V):
    visit = set()
    result = []
    queue = [V]
    visit.add(V)
    result.append(V)

    while queue:
        node = queue.pop(0)
        for neighbor in sorted(adj_list.get(node, [])):
            if neighbor not in visit:
                queue.append(neighbor)
                visit.add(neighbor)
                result.append(neighbor)

    return result

dfs(adj_list, V)

for n in result_dfs:
    print(n, end=' ')
print()
for n in bfs(adj_list, V):
    print(n, end=' ')



