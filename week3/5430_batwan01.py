from collections import deque

T = int(input())

for _ in range(T):
    order = input()
    N = int(input())
    '''try:
        que = deque(map(int,input().strip('[]').split(',')))
    except:
        print("error")
        continue'''
    
    arr = input()[1:-1]
    # 빈 배열 처리
    que = deque(arr.split(',')) if arr else []
    
    flag_R = False
    flag_error = False
    for ch in order:
        if ch == 'R':
            flag_R = not flag_R
        elif ch == 'D':
            if not que: 
                flag_error = True
                break
            if flag_R:
                que.pop()
            else:
                que.popleft()

    if flag_error:
        print("error")
    else:
        if flag_R:
            que.reverse()
        print(f"[{','.join(map(str,que))}]")