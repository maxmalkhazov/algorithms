num_1 = int(input('Enter first number: '))
num_2 = int(input('Enter second number: '))
num_3 = int(input('Enter third number: '))

def find_max_num(num_1, num_2, num_3):
    numbers = [num_1, num_2, num_3]
    return max(numbers)

print(find_max_num(num_1, num_2, num_3))