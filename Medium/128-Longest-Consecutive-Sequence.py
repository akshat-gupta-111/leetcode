'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

https://leetcode.com/problems/longest-consecutive-sequence/description/

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_ = set(nums)
        longest = 0
        for num in hash_:
            seq = 0
            if num-1 not in hash_:

                while num in hash_:
                    seq += 1
                    num = num + 1
            if seq > longest:
                longest = seq
        return longest