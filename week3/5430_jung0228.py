from collections import deque

T = int(input())

for _ in range(T):
    commands = input() 
    n = int(input())
    arr = input()[1:-1]
    # 빈 배열 처리
    l = arr.split(',') if arr else []
    flag = 1
    error = False

    for command in commands:
        if command == "R":
            flag *= -1
        elif command == "D":
            if not l:  # 배열이 비어있을 때
                error = True
                break
            if flag == 1:
                l.pop(0)
            else:
                l.pop()

    if error:
        print("error")
    else:
        if flag == -1:  # R 명령어 최종 처리
            l.reverse()
        print("[" + ",".join(l) + "]")

