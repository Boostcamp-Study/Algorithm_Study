import sys

# N = 100,000 : O(NlogN) **

def find_prime_list(n):
    is_prime = [True] * (n + 1)
    for i in range(2, int(n**0.5) + 1):
        for j in range(i * i, n + 1, i):
            is_prime[j] = False
    return is_prime 
        
is_prime = find_prime_list(1000000)
        
while True:
    is_goldbach = False
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        break
    for p1 in range(3, num, 2):
        if is_prime[p1] and is_prime[num-p1]:
            is_goldbach = True
            print(f"{num} = {p1} + {num-p1}")
            break
    if not is_goldbach:
        print("Goldbach's conjecture is wrong.")
            
        




