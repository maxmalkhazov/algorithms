test_string = 'AAAABBBCCCCCDDEEEE'

def compress_string(s):
    if len(s) == 0:
        return ""

    if len(s) == 1:
        return s + "1"

    compressed = ''
    count = 1
    i = 1

    while i < len(s):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed = compressed + s[i - 1] + str(count)
            count = 1
        i += 1

    compressed = compressed + s[i - 1] + str(count)

    return compressed

print(compress_string(test_string))

