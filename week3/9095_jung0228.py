n = int(input())

# 1, 2, 3 더하기 조합을 미리 만들어 두기 
dp = [1, 2, 4]
for i in range(3, 13):
    new = dp[i-1] + dp[i-2] + dp[i-3]
    dp.append(new) 

for _ in range(n):
    idx = int(input())
    print(dp[idx-1])
