unique_string = 'abcde'
non_unique_string = 'aabcde'

def unique_characters_in_string(s):
    count = {}

    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    for k in count:
        if count[k] > 1:
            return False

    return True


print(unique_characters_in_string(unique_string))
print(unique_characters_in_string(non_unique_string))


def uni_char(s):
    chars_set = set()

    for char in s:
        if char in chars_set:
            return False
        else:
            chars_set.add(char)

    return True

print(uni_char(unique_string))
print(uni_char(non_unique_string))