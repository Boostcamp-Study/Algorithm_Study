#6588 골드바흐의 추측

def is_odd_prime(n):
    for i in range(3, int(n**0.5)+1, 2):
        if n % i ==0:
            return 0
    return 1

def solution(N):
    for i in range(3, int(N/2)+1, 2):
        if is_odd_prime(i) == 1 and is_odd_prime(N-i):
            return print(f"{N} = {i} + {N-i}")
            
    print("Goldbach's conjecture is wrong.")

while True:
    N = int(input())
    if N == 0:
        break
    solution(N)