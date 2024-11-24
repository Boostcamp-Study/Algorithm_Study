import math
from functools import reduce
n = int(input())
n_list=[int(input()) for _ in range(n)]

interval=[n_list[i+1]-n_list[i] for i in range(n-1)] # 간격 list로 저장
gcd=reduce(math.gcd,interval) # 최대 공약수 구하기

res_list= sum((i // gcd - 1) for i in interval) # 간격/gcd-1 = 추가할 가로등의 수 의 전체 합
'''for i in range(n_list[0],n_list[-1]+1,gcd)로 전체 가로등의 
개수 구해서 len(n_list) 빼면 메모리 초과하기 때문에 합으로 계산'''

print(res_list)