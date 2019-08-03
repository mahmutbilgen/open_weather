'''
Leetcode Question

Source : https://leetcode.com/problems/merge-two-sorted-lists/

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4


'''

import math

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self):
        pass

    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        n = newList = ListNode(0)
        while l1 or l2:
            if l1:
                v1 = l1.val
            else:
                v1 = math.inf
            if l2:
                v2 = l2.val
            else:
                v2 = math.inf

            if v1 <= v2:
                newList.next = ListNode(v1)
                l1 = l1.next
                newList = newList.next
            else:
                newList.next = ListNode(v2)
                l2 = l2.next
                newList = newList.next
        return n.next

if __name__=='__main__':
    l1=ListNode(1)
    l1v2=ListNode(2)
    l1v4=ListNode(4)
    l1v2.next=l1v4
    l1.next=l1v2

    l2=ListNode(1)
    l2v3=ListNode(3)
    l2v4=ListNode(4)
    l2v3.next=l1v4
    l2.next=l2v3
    sol = Solution()
    n = ListNode(0)
    n = sol.mergeTwoLists(l1,l2)
    while (n.next):
        print(n.val)
        n=n.next
