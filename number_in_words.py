def number_to_words(n):

    to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
    tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
    thousand_and_up = ['Thousand', 'Million', 'Billion']
    
    def words(num):
        if num < 20:
            return to19[num-1:num]
        if num < 100:
            return [tens[num/10-2]] + words(num%10)
        if num < 1000:
            return [to19[num/100-1]] + ['Hundred'] + words(num%100)
        for p, w in enumerate(thousand_and_up, 1):
            if num < 1000**(p+1):
                return words(num/1000**p) + [w] + words(num%1000**p)

    return ' '.join(words(n)) or "Zero"

if __name__ == '__main__':
    print number_to_words(1129832261)
