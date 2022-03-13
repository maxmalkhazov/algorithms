test_string = 'bbbbbcaaaaa'
test_string_2 = 'aaaabbbb'

def split_in_half(s):
    if len(s) % 2 != 0:
        return s[(len(s) // 2) + 1:] + s[:len(s) // 2] + s[len(s) // 2]
    else:
        return s[len(s) // 2:] + s[:len(s) // 2]


print(split_in_half(test_string))
print(split_in_half(test_string_2))