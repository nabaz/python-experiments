'''
The balanced parentheses problem shown above is a specific case of a more
general situation that arises in many programming languages. The general
problem of balancing and nesting different kinds of opening and closing
symbols occurs frequently. For example, in Python square brackets,
[ and ], are used for lists; curly braces, { and }, are used for dictionaries;
 and parentheses, ( and ), are used for tuples and arithmetic expressions.
 It is possible to mix symbols as long as each maintains its own open and
 close relationship. Strings of symbols such as
'''

from helper.stack import Stack

def parentheses_checker(symb):
    s = Stack()

    balanced = True
    index = 0

    while index < len(symb) and balanced:
        symbol = symb[index]

        if symbol in "([{":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index = index + 1
    if balanced and s.is_empty():
        return True
    else:
        return False


def matches(open, close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)


print(parentheses_checker('{{([][])}()}'))
print(parentheses_checker('[{()]'))
