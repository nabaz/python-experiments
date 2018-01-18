'''
Determine whether an integer is a palindrome. Do this without extra space.

'''


def is_palindrome(n):

    return int(str(abs(n))[::-1]) == n


p = is_palindrome(1221)

print p
