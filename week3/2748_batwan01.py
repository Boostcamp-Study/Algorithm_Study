arr = [0,1,1]

N = int(input())

for i in range(3, N + 1):
    arr.append(arr[i-1] + arr[i-2])

print(arr[N])