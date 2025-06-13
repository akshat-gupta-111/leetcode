'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

https://leetcode.com/problems/group-anagrams/description/

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
'''


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict_ = {}

        for word in strs:
            freq = [0] * 26
            for char in word:
                freq[ord(char)-ord('a')] += 1
            if tuple(freq) not in dict_:
                dict_[tuple(freq)] = []
            dict_[tuple(freq)].append(word)
        return dict_.values()
                    
