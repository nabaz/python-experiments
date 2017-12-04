class NumberInWord:
    # TODO: finish the function
    NUMBERS_HASH = {
        90 : "ninety",   80 : "eighty",   70 : "seventy",
        60 : "sixty",    50 : "fifty",    40 : "forty",
        30 : "thirty",   20 : "twenty",   19 : "nineteen",
        18 : "eighteen", 17 : "seventeen",16 : "sixteen",
        15 : "fifteen",  14 : "fourteen", 13 : "thirteen",
        12 : "twelve",   11 : "eleven",   10 : "ten",
        9  : "nine",     8  : "eight",    7  : "seven",
        6  : "six",      5  : "five",     4  : "four",
        3  : "three",    2  : "two",      1  : "one",
    }
    def __init__(self, number):
        self.number = number

    def find_100s(self):
        str_ones = self.number % 10
        str_hundred = self.number // 100
        str_10th = self.number - ((str_hundred) * 100) - (str_ones)
        if self.number // 100 / 10 > 0:
            return "{} thousand".format(self.NUMBERS_HASH[self.number // 100 / 10])
        else:
            return "{} hundred {} {}".format(self.NUMBERS_HASH[str_hundred], self.NUMBERS_HASH[str_10th], self.NUMBERS_HASH[str_ones])

def toStr(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]

print(toStr(1000,16))

# n = NumberInWord(920)
# print(n.find_100s())
