'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

https://leetcode.com/problems/generate-parentheses/description/

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
'''



class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        stack = []
        res = []

        def backtrack(openN, closeN):
            if openN == closeN == n :
                res.append("".join(stack))
                return
            if openN < n :
                stack.append("(")
                backtrack(openN + 1, closeN)
                stack.pop()
            
            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN + 1)
                stack.pop()
                
        backtrack(0, 0)
        return res


