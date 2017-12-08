def is_zero(a_list):
    sum_of_zero = []

    for i in range(len(a_list)):
        for j in range (len(a_list[1::])):
            for x in range (len(a_list[2::])):
                sum_three = a_list[i] + a_list[j] + a_list[x]
                if sum_three == 0:
                    sum_of_zero.append([a_list[i] , a_list[j] , a_list[x]])

    return sum_of_zero


a = [1,2,-3,4,3,6,-1,2]
print is_zero(a)
