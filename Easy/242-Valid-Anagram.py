'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

https://leetcode.com/problems/valid-anagram/description/

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true


'''

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        freq_s = {}
        freq_t = {}
        for i in range(len(s)):
            freq_t[t[i]] = 1 + freq_t.get(t[i], 0)
            freq_s[s[i]] = 1 + freq_s.get(s[i], 0)         
        for count in freq_s:
            if freq_s[count] != freq_t.get(count, 0):
                return False
        return True
        