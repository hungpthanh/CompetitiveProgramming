# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None:
            return head
        def insert(p, head_part1):
            next_p = head_part1.next
            head_part1.next = p
            p.next = next_p


        def remove(last, p):
            last.next = p.next

        head = ListNode(-300, head)
        pointer = head

        while pointer.val < x and pointer.next is not None:
            last = pointer
            pointer = pointer.next
        if pointer.next is None:
            return head.next
        head_part1 = last

        while pointer is not None:
            if pointer.val < x:
                remove(last, pointer)
                insert(pointer, head_part1)
                head_part1 = pointer
                pointer = last.next
            else:
                last = pointer
                pointer = pointer.next
        return head.next