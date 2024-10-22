# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None:
            return head
        current = head
        if current.next is None:
            return current
        current_next = head.next
        new_head = self.reverseList(head.next)
        current_next.next = current
        current.next = None
        return new_head
        
        
