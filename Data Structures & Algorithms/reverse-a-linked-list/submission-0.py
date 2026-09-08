# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        tailing_node = ListNode(val=head.val)
        head = head.next

        while head:
            tmp = ListNode(val=head.val, next=tailing_node)
            tailing_node = tmp
            head = head.next

        return tailing_node
        