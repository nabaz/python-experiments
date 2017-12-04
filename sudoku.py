def sudoku2(grid):
    return  check_all_column(grid) and check_all_rows(grid) and check_sub_array(grid)

    def check_all_rows(grid):
    i = 0
    while i < len(grid):
        j = 0
        dic = {}
        while j < len(grid[i]):
            if grid[i][j] != '.' and grid[i][j] in dic:
                return False
            else:
                dic[grid[i][j]] = 0
            j += 1
        i += 1
    return True

def check_all_column(grid):
    i = 0
    l =  len(grid)
    column = 0
    while column < l:
        j = 0
        row = 0
        dic = {}
        while row < l:
            if grid[row][column] != '.' and grid[row][column] in dic:
                return False
            else:
                dic[grid[row][column]] = 0
            row +=1
        column += 1
    return True


def create_sub_grid(grid):
    dic = {}
    for e in grid:
        if e != '.' and e in dic:
            return False
        else:
            dic[e] = 0
    return True


def check_sub_array(grid):
    arr = []
    for row in range(0,9,3):
        for i in range(0,9, 3):
            a = []
            for j in range(row, row + 3):
                tmp = []
                for col in range(i, i + 3):
                    tmp.append(grid[j][col])
                a.append(tmp)
            arr.append(a)
    print(arr)

    arr = []
    for row in range(0,9,3):
        for i in range(0,9, 3):
            a = []
            for j in range(row, row + 3):
                for col in range(i, i + 3):
                    a.append(grid[j][col])
                    arr.append(a)
    for row in arr:
        if not create_sub_grid(row):
            return False
    return True
