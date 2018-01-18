def int_to_roman(num):

    v = [1000,900,500,400,100,90,50,40,10,9,5,4,1]

    roman = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]

    res = ""

    for n, val in zip(roman, v):
        res += (num // val) * n
        print n, val, res
        num %= val

    return res



print int_to_roman(1904)
