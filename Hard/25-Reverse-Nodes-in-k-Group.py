'''
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

https://leetcode.com/problems/reverse-nodes-in-k-group/description/

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0, head)
        grpPrev = dummy

        while True:
            kth = self.getKth(grpPrev, k)
            if  not kth:
                break
            grpNext = kth.next

            prev, curr = kth.next, grpPrev.next
            while curr != grpNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            tmp = grpPrev.next
            grpPrev.next = kth
            grpPrev = tmp
        return dummy.next

    def getKth(self, curr, k):
            while curr and k  > 0:
                curr = curr.next
                k = k - 1
            return curr