# Definition for singly-linked list.
# Question : https://leetcode.com/problems/merge-two-sorted-lists/
# !!! There are some errors

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class ListNode:
    def __init__(self, headval):
        HeadNode = Node(headval)
        self.head = HeadNode
        #self.next = None

    def __init__(self, alist):
        aVal = alist.get(0)
        HeadNode = Node(aVal)
        self.head = HeadNode
        for i in alist:
            self.add_end(i)

    def add_end(self, data):
        NewNode = Node(data)
        last = self.head
        while (last.next is not None):
            last = last.next
        last.next = NewNode

    def sort(self, l1, l2):
        pass


class Solution:
    def __init__(self):
        pass
        #sol_list = ListNode(headval)

    # def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    def mergeTwoLists(l1: ListNode, l2: ListNode):
        print("mergeTwoLists")

    def print_list(aList):
        print("print result")
        ptr_node = aList.head
        print(ptr_node.data)
        while (ptr_node.next is not None):
            ptr_node = ptr_node.next
            print(ptr_node.data)


if __name__ == '__main__':
    aList = [1, 2, 4]
    l1 = ListNode(aList)

    # l1 = ListNode(1)
    # l1.add_end(2)
    # l1.add_end(4)

    l2 = ListNode(1)
    l2.add_end(3)
    l2.add_end(4)

    Solution.mergeTwoLists(l1, l2)
    Solution.print_list(l1)
    Solution.print_list(l2)
