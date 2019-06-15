#!/usr/local/bin/python3.7
import os

class Node:
    def __init__(self,data_value=None):
        self.data_value=data_value
        self.next_value=None
        self.pre_value=None
        self.down_value=None
    def setNextValue(self,next_node):
        self.next_value=next_node

class aLinkedList:
    def __init__(self):
        self.head_value=None

    def print_list(self):
        print_value = self.head_value
        while print_value is not None:
            print (print_value.data_value)
            print_value = print_value.next_value


if __name__=='__main__' :
    alist = aLinkedList()
    alist.head_value = Node("Mon")
    e2 = Node("Tue")
    e3 = Node("Wed")

    alist.head_value.setNextValue(e2)

    if e2.next_value is  None:
        e2.setNextValue(e3)

    alist.print_list()
