def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    nums.sort()
    for i in xrange(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l +=1
            elif s > 0:
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1, r -= 1
    return res

'''
nums.sort()
solution = []
for idx,tgt in enumerate(nums):
    if idx>0 and nums[idx] == nums[idx-1]:
        continue
    path = {}
    vist = set()
    for i in xrange(idx+1,len(nums)):
        if nums[i] not in path:
            path[-tgt-nums[i]] = nums[i]
        elif nums[i] in path and nums[i] not in vist:
            solution.append([tgt,path[nums[i]],nums[i]])
            vist.add(nums[i])

return solution
'''

s = [-1, 5, 3, 2, -1, -5]
three = threeSum(s)
print three
