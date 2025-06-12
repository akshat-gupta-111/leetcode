'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 https://leetcode.com/problems/contains-duplicate/description/

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

'''


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        x = set()
        for num in nums:
            if num not in x:
                x.add(num)
            else:
                return True
        return False