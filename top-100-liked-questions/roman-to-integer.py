''''
Given a roman numeral, convert it to an integer.
Input is guaranteed to be within the range from 1 to 3999.
Input : IX
Output : 9

Input : XL
Output : 40

Input : MCMIV
Output :  1904
M is a thousand, CM is nine hundred
and IV is four
'''


def roman_to_integer(s):

    roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

    res, p = 0, 'I'
    for c in s[::-1]:
        res, p = res - roman[c] if roman[c] < roman[p] else res + roman[c], c
        print s, p
    return res

print roman_to_integer('MCMIV')
