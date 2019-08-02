class ListNode:


def init(self, x):


self.val = x
self.next = None


class Solution:


def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:


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
