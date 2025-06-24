'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

https://leetcode.com/problems/search-a-2d-matrix/description/

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
'''

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows,cols = len(matrix), len(matrix[0])

        up,btm = 0, rows - 1
        while up <= btm:
            row = (up + btm) // 2
            if matrix[row][-1] < target:
                up = row + 1
            elif matrix[row][0] > target:
                btm = row - 1
            else:
                break
        if up > btm:
            return False
        l, r = 0, cols - 1
        while l <= r:
            mid = (l + r)//2
            if (matrix[row])[mid] == target:
                return True
            elif (matrix[row])[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False