'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

https://leetcode.com/problems/product-of-array-except-self/description/

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

'''

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = [1] * len(nums)
        i = 0
        j = len(nums) - 1
        pre = 1
        post = 1
        while i < len(nums) and j >= 0:
            if (i != 0):
                answer[i] *= (nums[i-1] * pre)
                pre *= nums[i-1]
            else:
                answer[i] *= pre
            if  j != len(nums) - 1:
                
                answer[j] *= (nums[j+1] * post)
                post *= nums[j+1]
                
            else:
                answer[j] *= post
            
            
            i+=1
            j-=1
        return answer