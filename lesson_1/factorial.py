import math

num = int(input('Input your number: '))

# print(math.factorial(num))






result = 1

if num != 0:
    for i in range(1, num + 1):
        result *= i

print(result)
