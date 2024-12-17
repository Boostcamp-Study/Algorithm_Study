#6588 골드바흐의 추측
import sys

def find_prime_list(n):
    is_prime = [True] * (n + 1)
    for i in range(2, int(n**0.5) + 1):
        for j in range(i * i, n + 1, i):
            is_prime[j] = False
    return is_prime 
        
odd_prime_list = find_prime_list(1000000)

def solution(N):
    for i in range(3, int(N/2)+1, 2):
        if odd_prime_list[i] and odd_prime_list[N-i]:
            print(f"{N} = {i} + {N-i}")
            return
            
    print("Goldbach's conjecture is wrong.")

while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    solution(N)