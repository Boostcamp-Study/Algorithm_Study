# 9935 문자열 폭발

string = input()
explode_string = input()

def solution(string, explode_string):
    stack = []
    count = 0
    for char in string:
        stack.append(char)
        if len(stack) >= len(explode_string) and ''.join(stack[-len(explode_string):]) == explode_string:
            for _ in range(len(explode_string)):
                stack.pop()

    if stack:
        return ''.join(stack)
    else:
        return 'FRULA'

print(solution(string, explode_string))