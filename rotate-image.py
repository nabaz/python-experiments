#Note: Try to solve this task in-place (with O(1) additional memory),
#since this is what you'll be asked to do during an interview.

#You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).

def rotateimage(a):
    b = zip(*a[::-1])
    return [i for i in b]


a = [[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]

print(rotateimage(a))
