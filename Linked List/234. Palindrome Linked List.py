# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        node = None
        
        while slow:
            n = slow.next
            slow.next = node
            node = slow
            slow = n
            
        while node:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True
            
        
