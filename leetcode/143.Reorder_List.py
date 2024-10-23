# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        Q = deque()
        cnt = 0
        while (head.next is not None):
            Q.append(head)
            head = head.next
        Q.append(head)
        head = ListNode(0, None)
        while (len(Q) > 1):
            head.next = Q[0]
            head.next.next = Q[-1]
            Q.pop()
            Q.popleft()
            head = head.next.next
        if len(Q) == 1:
            head.next = Q[0]
            head = head.next
        head.next = None
        head = head.next


        
