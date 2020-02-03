# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        first,second = head,head
        
        for i in range(n):
            first = first.next
            
        if first is None:
            if second.next is not None:
                head = head.next
                return head
            head = None
            return None
        
        
        while first.next is not None:
            second = second.next
            first = first.next
        second.next = second.next.next
        
        return head
        
