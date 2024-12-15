import math

def double(n1, n2):
    if n1 == 0: 
        return -1
    if n1 < n2:  
        if n2 % (2 * n1) == 0:
            log_n1 = math.log2(n2 // (2 * n1))
            if log_n1.is_integer():
                return int(log_n1) + 1
        return -1
    else: 
        n1 = (2 * n1) % 10000 
        if n1 == n2:
            return 1
        return -1

def diff(n1, n2):
    return min(abs(n1 - n2), 9999 - abs(n1 - n2) + 1)
    
def shift(n1, n2, direction):
    a = str(n1).zfill(4)
    b = str(n2).zfill(4)
    count = 0
    for _ in range(len(a)):
        if int(a) == int(b):
            return count
        if direction == "L":
            a = a[1:] + a[0]
        else:
            a = a[-1] + a[:-1]
        count += 1
    return -1

N = int(input())
for _ in range(N):
    n1, n2 = map(int, input().split())
    min_count = float('inf')
    flag = None

    count_double = double(n1, n2)
    if count_double != -1 and count_double < min_count:
        min_count = count_double
        flag = "D"

    count_diff = diff(n1, n2)
    if count_diff < min_count:
        min_count = count_diff
        flag = "S"

    count_L = shift(n1, n2, "L")
    if count_L != -1 and count_L < min_count:
        min_count = count_L
        flag = "L"

    count_R = shift(n1, n2, "R")
    if count_R != -1 and count_R < min_count:
        min_count = count_R
        flag = "R"

    if flag == "D":
        print("D" * min_count)
    elif flag == "S":
        print("S" * min_count)
    elif flag == "L":
        print("L" * min_count)
    elif flag == "R":
        print("R" * min_count)