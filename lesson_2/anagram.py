str_1 = "abcd"
str_2 = "dabc"

def anagram(str_1, str_2):
    list_1 = []
    list_2 = []

    for c in str_1:
        list_1.append(c)

    for c in str_2:
        list_2.append(c)

    list_1.sort()
    list_2.sort()

    if list_1 == list_2:
        return "Anagram"
    else:
        return "Not angram"


def anagram_opt(str_1, str_2):
    if len(str_1) != len(str_2) or sorted(str_1) != sorted((str_2)):
        return "Not anagram"
    else:
        return "Anagram"



def anagram_long(str_1, str_2):
    count = {}
    for letter in str_1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in str_2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return "Not anagram"

    return "Anagram"

print(anagram_long(str_1, str_2))
