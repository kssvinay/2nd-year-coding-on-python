# https://leetcode.com/problems/reverse-linked-list-ii/description/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        ans = ListNode(0)
        aa = ans
        i = 1
        reverse = None
        while head:
            print(reverse)
            if i>=left and i<=right:
                if not reverse:
                    reverse = ListNode(head.val)
                else:
                    p = ListNode(head.val)
                    p.next = reverse
                    reverse = p
                ans.next = reverse
            else:
                if reverse:
                    while reverse:
                        ans.next = reverse
                        ans = ans.next
                        reverse = reverse.next
                ans.next = ListNode(head.val)
                ans = ans.next
            head = head.next
            i += 1
        return aa.next
