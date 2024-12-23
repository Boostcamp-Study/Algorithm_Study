h, m, s = map(int,input().split())
time = int(input())

total_seconds = h * 3600 + m * 60 + s + time

h = (total_seconds // 3600) % 24
m = (total_seconds % 3600) // 60
s = total_seconds % 60

print(h, m, s)