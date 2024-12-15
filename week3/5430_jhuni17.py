# 5430 AC

from collections import deque

T = int(input())

def solution(p, n, arr):
    arr = deque(arr)
    flag = 1
    for func in p:
        if func == 'R':
            flag *= -1
        else:
            if not arr:
                return 'error'
            if flag == 1:
                arr.popleft()
            else:
                arr.pop()

    if flag == 1:
        return '['+','.join(map(str, list(arr)))+']'
    else:
        return '['+','.join(map(str, list(reversed(arr))))+']'


result = []
for _ in range(T):
    p = str(input())
    n = int(input())
    if n == 0:
        _ = input()
        arr = []
    else:
        arr = list(map(int, input().strip('[]').split(',')))
    result.append(solution(p, n, arr))

for r in result:
    print(r)