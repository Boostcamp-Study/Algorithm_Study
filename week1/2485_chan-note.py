import sys
from math import gcd
from functools import reduce
'''
1초 기준 python
N <= 500 : O(N^3)
N <= 2,000 : O(N^2)
N <= 100,000 : O(NlogN) **
N <= 10,000,000 : O(N)
'''

# 풀이1 : 시간복잡도 O(NlogK) = O(NlogN) (K=N-1)
# 입력
N = int(sys.stdin.readline().rstrip())
tree = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

# diff list 생성
distance = [tree[i+1]-tree[i] for i in range(len(tree)-1)]

# 최대공약수 계산: gcd
gcd = reduce(gcd, distance)

# 심어야하는 나무 갯수 계산
count = 0
for dist in distance:
    count += (dist//gcd) - 1

# 출력
sys.stdout.write(str(count))
