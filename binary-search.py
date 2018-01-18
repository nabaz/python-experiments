def binary_search(a_list, item):
    if len(a_list) == 0:
        return False
    else:
        mid = len(a_list) // 2
        if a_list[mid] == item:
            return True
        else:
            if item < a_list[mid]:
                return binary_search(a_list[:mid], item)
            else:
                return binary_search(a_list[mid+1:], item)

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,13]
print binary_search(testlist, 42)
