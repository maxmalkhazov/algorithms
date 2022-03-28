test_list = [198, 3, 4, 9, 10, 9, 2]

def lowest_elements(arr):

    if len(arr) < 2:
        return "Please enter a valid list"

    arr.sort()

    result = arr[0], arr[1]

    return result

print(lowest_elements(test_list))