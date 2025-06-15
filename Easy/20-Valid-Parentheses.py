'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

https://leetcode.com/problems/valid-parentheses/description/

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        match = {')' : '(', ']' : '[', '}' : '{'}
        stack = []

        for b in (s):
            if b in match:
                if stack and stack[-1] == match[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        return stack == []


                  