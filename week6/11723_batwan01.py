'''
add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
all: S를 {1, 2, ..., 20} 으로 바꾼다.
empty: S를 공집합으로 바꾼다.
'''
import sys

def add(S, x):
    S.add(x)

def remove(S, x):
    S.discard(x)

def check(S, x):
    print(1 if x in S else 0)

def toggle(S, x):
    if x in S:
        S.remove(x)
    else:
        S.add(x)

def all(S):
    S.update(range(1, 21))

def empty(S):
    S.clear()

N = int(sys.stdin.readline().rstrip())
S = set()

for _ in range(N):
    command = sys.stdin.readline().rstrip().split()
    func = command[0]
    
    if func in ['add', 'remove', 'check', 'toggle']:
        num = int(command[1])
        if func == 'add':
            add(S, num)
        elif func == 'remove':
            remove(S, num)
        elif func == 'check':
            check(S, num)
        elif func == 'toggle':
            toggle(S, num)
    elif func == 'all':
        all(S)
    elif func == 'empty':
        empty(S)