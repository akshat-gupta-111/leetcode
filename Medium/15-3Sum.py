'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

https://leetcode.com/problems/3sum/description/

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res =[]
        nums.sort()
        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and nums[i - 1] == a:
                continue
            j = i + 1
            k = len(nums) - 1 
            while j < k:
                target = a + nums[j] + nums[k]
                if target > 0:
                    k -= 1
                elif target < 0:
                    j += 1
                else:
                    res.append([a,nums[j],nums[k]])
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j+=1
            
        return res
                
        