from collections import deque

T = int(input())

for _ in range(T):
    commands = input() 
    n = int(input())
    R_cnt = commands.count('R')
    # str to list 
    l = input()[1:-1].split(',')
    flag = 1

    for i in range(len(commands)): 
        command = commands[i] 

        print(command, len(l), l)


        if command == "R":
            flag *= -1
        elif command == "D" and len(l) > 0:
            if  flag == 1:  
                l.pop(0)
            else: 
                l.pop()
        else:
            print("error")
            continue

    # R이 홀수면 뒤집기 연산 
    if R_cnt%2 == 1:
        l = l[::-1]    

    # str로 출력
    if len(l) >= 0:
        l = "[" + ",".join(l) + "]"
        print(l)    
    else:
        print("error")

