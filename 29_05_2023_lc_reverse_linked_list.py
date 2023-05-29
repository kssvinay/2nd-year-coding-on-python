# https://leetcode.com/problems/reverse-linked-list/description/

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        k = None
        while head:
            p = ListNode(head.val)
            p.next = k
            k = p
            head = head.next
        return k
      
