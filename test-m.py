#input [[1,2],[3,4], [6,10]]
#output [[1,4],[6,10]]

from itertools import groupby
from operator import itemgetter

def findNumRang(a_list):
    new_list = [a_list[0],]
    temp_list = []

    for i, (s, e) in enumerate(a_list[1:]):
        if s <= max(new_list[i]) + 1:
            new_list.append([min(new_list[i]), e])
            temp_list = new_list[:]
            temp_list.pop(0)
        elif s >  max(new_list[i]):
            new_list.append([s,e])
            temp_list = new_list[:]
            temp_list.pop(0)

    return temp_list

a = [[1,2],[3,4],[7,10]]
print(findNumRang(a))
