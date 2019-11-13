'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.

Example 1:
Input: [1,3,5,6], 5
Output: 2

Example 2:
Input: [1,3,5,6], 2
Output: 1
'''

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        ##Intuitive solution: loop through values till find the correction index
        i = 0
        while nums[i] <= target:
            if nums[i] < target:
                i += 1
            if nums[i] == target:
                return i

        return i+1

        ##Binary search solution: search from both sides
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r)/2 #using (l+r)//2 in python 3.
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return l
