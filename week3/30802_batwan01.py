'''
첫 줄에 티셔츠를 
T장씩 최소 몇 묶음 주문해야 하는지 출력하세요.

다음 줄에 펜을 
P자루씩 최대 몇 묶음 주문할 수 있는지와, 그 때 펜을 한 자루씩 몇 개 주문하는지 구하세요.
'''

N = int(input())
arr = list(map(int, input().split()))
T, P = map(int, input().split())

T_count = 0
P_count = 0
P_add = 0

for num in arr:
    if num%T == 0:
        T_count += num//T
    else:
        T_count += num//T + 1
        
print(f'{T_count}\n{N//P} {N%P}')