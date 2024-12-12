'''
 $i$가 $3$의 배수이면서 $5$의 배수이면 “FizzBuzz”를 출력합니다.
 $i$가 $3$의 배수이지만 $5$의 배수가 아니면 “Fizz”를 출력합니다.
 $i$가 $3$의 배수가 아니지만 $5$의 배수이면 “Buzz”를 출력합니다.
 $i$가 $3$의 배수도 아니고 $5$의 배수도 아닌 경우 $i$를 그대로 출력합니다.
'''

arr = []
count = 3
for _ in range(3):
    arr.append(input())

for num in arr:
    if num.isdigit():
        num_result = int(num) + count
        if num_result % 5 == 0 and num_result % 3 == 0:
            print("FizzBuzz")
        elif num_result % 3 == 0:
            print("Fizz")
        elif num_result % 5 == 0:
            print("Buzz")
        else:
            print(num_result)
        break
    else:
        count-=1