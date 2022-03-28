first = [1,2,3,4,5,6,7]
second = [3,7,2,1,4,6]

def find_missing_element(list_1, list_2):
    list_1.sort()
    list_2.sort()

    for num1, num2 in zip(list_1, list_2):
        if num1 != num2:
            return num1

    return list_1[-1]

print(find_missing_element(first, second))

import collections

def dict_solution(list_1, list_2):
    dict = collections.defaultdict(int)

    for num in list_2:
        dict[num] += 1

    for num in list_1:
        if dict[num] == 0:
            return num
        else:
            dict[num] -= 1


print(find_missing_element(first, second))