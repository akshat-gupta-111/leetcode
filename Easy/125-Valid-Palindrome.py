'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

https://leetcode.com/problems/valid-palindrome/description/

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
'''

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1
        while i <= j:
            if not ((ord('a') <= ord(s[i].lower()) <= ord('z')) or (ord('0') <= ord(s[i].lower()) <= ord('9'))):
                i += 1
                continue
            if not ((ord('a') <= ord(s[j].lower()) <= ord('z')) or (ord('0') <= ord(s[j].lower()) <= ord('9'))):
                j-=1
                continue
            if i < len(s) and j >= 0:
                if s[i].lower() != s[j].lower():
                    return False
            j -= 1
            i += 1
        return True