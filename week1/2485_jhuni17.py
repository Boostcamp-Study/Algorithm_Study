# 가로수 위치가 주어지고 기준점으로 부터 오름차순
# 처음 가로수 사이 거리의 최대 공약수 구하기
# 위에서 구한 최대 공약수와 그 다음 간격의 최대 공약수 반복해서 구하기
# 최종적으로 나온 최대 공약수가 가로수간 최대 가능한 간격 

N = int(input())
trees = []
for _ in range(N):
    trees.append(int(input()))

def gcd(m, n):
    if m < n:
        m, n = n, m
    if n == 0:
        return m
    if m % n == 0:
        return n
    else:
        return gcd(n, m % n)

def solution(N, trees):
    gap_gcd = trees[1] - trees[0]
    for i in range(N-2):
        gap_gcd = gcd((trees[i+2] - trees[i+1]), gap_gcd)

    return (trees[-1] - trees[0]) // gap_gcd - N + 1
        
print(solution(N, trees))