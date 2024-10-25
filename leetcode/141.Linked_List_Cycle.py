# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        M = set()
        M.add(head)
        while (head.next is not None):
            if head.next in M:
                return True
            M.add(head.next)
            head = head.next
        return False
            
        
