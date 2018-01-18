'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''
def twoSum(nums, target):
    if len(nums) <= 1:
        return False
    my_dict = {}
    for i in range(len(nums)):
        if nums[i] in my_dict:
            return [my_dict[nums[i]], i]
        else:
            my_dict[target - nums[i]] = i
