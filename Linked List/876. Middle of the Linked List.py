# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        while(head and head.next):
            slow = slow.next
            head = head.next.next
        
        return slow
