palindrome = "radar"
not_palindrome = "radix"

def pal(str):
    if str == str[::-1]:
        return "Palindrome"
    else:
        return "Not palindrome"


print(pal(palindrome))
print(pal(not_palindrome))