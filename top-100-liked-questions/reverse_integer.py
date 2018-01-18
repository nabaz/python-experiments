'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range.
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''
def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    sign = lambda x: x and (1, -1)[x < 0]
    r = int(str(sign(x)*x)[::-1])
    return (sign(x)*r, 0)[r > 2**31 - 1]
