almost_a_palindrome = "radkar"
not_almost_a_palindrome = "radario"

def almost_a_pal(s):
    if len(s) == 0 or s == s[::-1]:
        return False

    for l in s:
        if l == l.upper():
            return False

    for l in range(len(s)):
        s_temp = s[:l] + s[l + 1:]
        if s_temp == s_temp[::-1]:
            return True

    return False




print(almost_a_pal(almost_a_palindrome))
print(almost_a_pal(not_almost_a_palindrome))
print(almost_a_pal(""))
print(almost_a_pal("Radkar"))
print(almost_a_pal("radar"))