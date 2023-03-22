class solution:
    def linkedlistcycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head