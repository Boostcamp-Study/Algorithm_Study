prime_set= set(range(2, 1000000+1))
for i in range(2, 1000000+1):
    if i in prime_set:
        prime_set -= set(range(2*i, 1000000+1, i))

prime_list = list(prime_set)

def binary_search(n):
    start = 0 
    end = len(prime_list) - 1

    while start <= end:  
        mid = (start+end) // 2

        if n == prime_list[mid]:
            return mid 
        elif n < prime_list[mid]: 
            end = mid - 1 
        else: 
            start = mid + 1 
     
    return end 

while True:
    n = int(input())

    if n==0: 
        break 
    
    k = binary_search(n)
    big_prime = prime_list[k]

    while(big_prime >= (n//2)):

        small_prime = n-big_prime

        if small_prime in prime_set: 
            print(f"{n} = {small_prime} + {big_prime}")
            break

        k -= 1
        big_prime = prime_list[k]
        
    if big_prime < n//2:
        print("Goldbach's conjecture is wrong.")
