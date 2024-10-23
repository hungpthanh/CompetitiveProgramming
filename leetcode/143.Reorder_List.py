# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# TLE
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head is None:
            return head
        if head.next is None:
            return head
        current = head
        while (current.next is not None):
            # print(current.val)
            prev = current
            current = current.next
        prev.next = None
        current.next = self.reorderList(head.next)
        head.next = current
        return head
        
