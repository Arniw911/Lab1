def is_palindrome(string):
    newstr = ''.join(reversed(string))
    return newstr == string

print(is_palindrome("lalal"))
    