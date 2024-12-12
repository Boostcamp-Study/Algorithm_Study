l = list(map(int, input().split()))

if l == sorted(l):
  print('ascending')
elif l == sorted(l, reverse=True):
  print('descending')
else:
  print('mixed')