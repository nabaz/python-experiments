'''
Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.

Input: "cbbd"

Output: "bb"

'''
def longest_palindorm_string(s):
    maxLength = 1

    start = 0
    length = len(s)

    low = 0
    high = 0

    # One by one consider every character as center point of
    # even and length palindromes
    for i in xrange(1, length):
        # Find the longest even length palindrome with center
    # points as i-1 and i.
        low = i - 1
        high = i
        while low >= 0 and high < length and s[low] == s[high]:
            if high - low + 1 > maxLength:
                start = low
                maxLength = high - low + 1
            low -= 1
            high += 1

        # Find the longest odd length palindrome with center
        # point as i
        low = i - 1
        high = i + 1
        while low >= 0 and high < length and s[low] == s[high]:
            if high - low + 1 > maxLength:
                start = low
                maxLength = high - low + 1
            low -= 1
            high += 1
    return s[start:start + maxLength]
