'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

https://leetcode.com/problems/top-k-frequent-elements/submissions/1662668075/

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
'''

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        k_el = []
        hash = {}
        bucket = [[] for _ in range(0,len(nums)+1)]
        for i in range(len(nums)):
            hash[nums[i]] = 1 + hash.get(nums[i], 0)
        for x in hash:
            bucket[hash[x]].append(x)
        for j in range(len(bucket)-1,-1,-1):
                if (bucket[j] != []):
                    for y in bucket[j]:
                        k_el.append(y)
                        if len(k_el)==k : return k_el