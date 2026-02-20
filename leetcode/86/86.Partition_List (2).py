# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_head, greater_head = ListNode(), ListNode()
        less_tail, greater_tail = less_head, greater_head

        while head:
            if head.val < x:
                less_tail.next = head
                less_tail = head
            else:
                greater_tail.next = head
                greater_tail = head
            head = head.next
        greater_tail.next = None
        less_tail.next = greater_head.next
        return less_head.next