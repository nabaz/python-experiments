def two_sum(a, s):

    my_dict= {}
    for i in range(len(a)):
        if a[i] in my_dict:
            return [my_dict[a[i]], i]
        else:
            my_dict[s - a[i]] = i
    return my_dict

print two_sum([1,5,-1,7], 6)
