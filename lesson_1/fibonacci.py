
def fib(n):

    result = [1, 1]

    if n < 0:
        return 'Not a valid value'
    if n == 0:
        return 0
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]

    result = [1, 1]
    index = 3

    while index <= n:
        result.append(result[-1] + result[-2])
        index = index + 1
    return result

print(fib(6))