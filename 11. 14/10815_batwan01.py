# 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.

'''
5
6 3 2 10 -10
8
10 9 -5 2 3 4 5 -10

output
1 0 0 1 1 0 0 1
'''

N = int(input())
my_card = set(map(int, input().split()))  # Use a set for faster lookups

M = int(input())
check_card = list(map(int, input().split()))

for num in check_card:
    if num in my_card:
        print(1, end=' ')
    else:
        print(0, end=' ')