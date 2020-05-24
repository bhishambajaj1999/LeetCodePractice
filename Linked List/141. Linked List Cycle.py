# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        try:
            s,f = head,head
            while s or f or f.next:
                s = s.next
                f = f.next.next
                if f == s:
                    return True
        except:
            return False
