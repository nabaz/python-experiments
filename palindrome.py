def is_palindrome(string):
    return string[::-1].lower().strip() == string.lower().strip()

print(is_palindrome("level "))
