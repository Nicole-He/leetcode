'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

#1. Brute Force Method
####Complexity: O(n^2)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums == []:
            return nums
        if len(nums) == 1:
            if nums[0] == target:
                return nums
            else:
                return []

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return([i,j])


#2. Hashtable Method
###Complexity: O(n)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        for i in range(len(nums)):
            if (target - nums[i]) in nums_dict:
                return([nums_dict[target-nums[i]], i])
            else:
                nums_dict[nums[i]] = i
