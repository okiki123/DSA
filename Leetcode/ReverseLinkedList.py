# Given the head of a singly linked list, reverse the list, and return the reversed list.
class ListNode:
    def __init__(self,  val):
        self.val =  val
        self.next = None
class Solution:
    def reverseList(self, head: ListNode)  -> ListNode:
        prev, curr = None, head
        
        while curr:
            nxt  = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


#Recursive Solution


