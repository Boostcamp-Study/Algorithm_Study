n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

# dp 배열을 미리 계산하여, 최대 n까지 처리 가능하게 확장
dp = [1, 2, 4]  # n = 1, n = 2, n = 3에 대한 초기값 설정

for i in range(3, 10):
    dp.append(dp[i-1] + dp[i-2] + dp[i-3])

# 각 테스트 케이스에 대해 결과 출력
for n in arr:
    print(dp[n-1])