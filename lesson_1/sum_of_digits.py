n = int(input('Enter number: '))

def sum_of_digits(n):
    result = 0
    if n < 0:
        return 'Please enter a valid number'
    else:
        while n > 0:
            result += n
            n = n - 1
    return result


print(sum_of_digits(n))