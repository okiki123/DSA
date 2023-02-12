# Given the head of a singly linked list, reverse the list, and return the reversed list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        