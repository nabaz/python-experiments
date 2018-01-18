'''
Given a matrix of m x n elements (m rows, n columns),
return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
'''
def spiral_order(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    return matrix and matrix.pop(0) + spiral_order([list(x) for x in zip(*matrix)][::-1])
