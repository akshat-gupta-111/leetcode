'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        dummy.next = head
        left = dummy
        right = head
        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next
        