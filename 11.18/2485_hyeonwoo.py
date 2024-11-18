# 2485번 문제
# 문제 링크: https://www.acmicpc.net/problem/2485

# 문제 설명
# 가로수들이 모두 같은 간격이 되도록 가로수를 추가로 심는다.
# 최소한의 가로수를 심기 위해서 추가로 심는 가로수의 수를 구하는 문제

# 풀이 방법 
# 1. 간격을 모두 구한다. 
# 2. 간격들의 최대공약수를 구한다.
# 3. 전체 길이에서 최대공약수를 나누고 원래 심어진 나무 개수를 뺀다.

import math

N = int(input()) 
tree_location = []
for i in range(N): 
  tree_location.append(int(input())) 

tree_interval = [] 
for i in range(1, N): 
  tree_interval.append(tree_location[i] - tree_location[i-1]) 

gcd = tree_interval[0]
for i in range(1, len(tree_interval)):
  gcd = math.gcd(gcd, tree_interval[i])

print((tree_location[-1] - tree_location[0]) // gcd - (N - 1))