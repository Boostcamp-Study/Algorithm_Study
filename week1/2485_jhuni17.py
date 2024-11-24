# 가로수 위치가 주어지고 기준점으로 부터 오름차순
# 기존의 가로수 간 최대 간격 수 부터 구하기

N = int(input())
trees = []
for _ in range(N):
    trees.append(int(input()))

def solution(N, trees):
    max_gap = int((trees[-1] - trees[0]) / (N-1))
    for gap in range(max_gap, 1, -1):
        check = [i for i in range(trees[0], trees[-1]+1, gap)]
        if len(set(trees)-set(check)) == 0:
            return len(check) - len(trees)
        
result = solution(N, trees)
print(result)