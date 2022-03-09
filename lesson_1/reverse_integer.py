


def reverse_integer(num):
    str_num = str(num)

    if str_num[0] == '-':
        return int('-' + str_num[:0:-1])
    else:
        return str_num[::-1]

print(reverse_integer(123))
print(reverse_integer(-456))