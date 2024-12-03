# 점화식 f(x) = f(x-1) + f(x-2) + f(x-3)

T = int(input())

arr = []
for _ in range(T):
    arr.append(int(input()))

def solution(n):
    dp = [1, 2, 4]
    for i in range(11):
        dp.append(dp[i+2] + dp[i+1] + dp[i])
    
    return dp[n-1]

for n in arr:
    print(solution(n))