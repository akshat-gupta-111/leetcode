'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

https://leetcode.com/problems/add-two-numbers/description/

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        cur = dummy
        carry = 0
        while l1 or l2 or carry:
            vl1 = l1.val if l1 else 0
            vl2 = l2.val if l2 else 0

            value = vl1 + vl2 + carry

            carry = value // 10
            cur.next = ListNode(value % 10)

            cur = cur.next
            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0

        return dummy.next