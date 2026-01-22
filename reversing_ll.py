# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Time Complexity: O(n) - single pass through linked list
        # Space Complexity: O(1) - only using constant extra space
        prev,curr=None,head

        while curr:
            next_val=curr.next
            curr.next=prev
            prev=curr
            curr=next_val
        return prev
