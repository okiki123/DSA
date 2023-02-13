# Given the head of a singly linked list, reverse the list, and return the reversed list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


#Doubly LinkedList
class Node:
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = None
        self.next = None
class  LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(data = new_data)
        new_node.next = self.head
        new_node.prev = None
        
        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node
