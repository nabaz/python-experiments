def spiral_order(matrix):
    return matrix and matrix.pop(0) + spiral_order([list(x) for x in zip(*matrix)][::-1])

a = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

b = spiral_order(a)

print b
