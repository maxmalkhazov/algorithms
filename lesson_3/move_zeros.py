
test_arr = [0, 4, 0, 3, 12]

def move_zeros(arr):

    i = 0

    for num in arr:
        if num != 0:
            arr[i] = num
            i += 1

    while i < len(arr):
        arr[i] = 0
        i += 1


    return arr

print(move_zeros(test_arr))