
test_list = [1, 3, 5, 6, 4, 10, 2, 3]

def below_mean(arr):
    sum = 0
    result = []
    for num in arr:
        sum += num

    mean = sum / len(arr)

    for num in arr:
        if num < mean:
            result.append(num)

    return result

print(below_mean(test_list))