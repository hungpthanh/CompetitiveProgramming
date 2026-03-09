# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        index = 0
        
        newHead = ListNode(-1, head)
        pointer = newHead
        left += 1
        right += 1
        index = 1
        st, en, le, ri = None, None, None, None
        while pointer is not None:
            if index == left - 1:
                st = pointer
            if index == right + 1:
                en = pointer
            if index == left:
                le = pointer
            if index == right:
                ri = pointer
            pointer = pointer.next
            index += 1
        
        pair = (le, le.next)
        while pair[0] is not ri:
            new_pair = (pair[1], pair[1].next)
            pair[1].next = pair[0]
            pair = new_pair
        st.next = ri
        le.next = en
        return newHead.next