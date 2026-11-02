# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next
        
        curr = head
        while True:
            nxt = curr.next
            node = stack.pop()
            if node == nxt or node == curr:
                node.next = None
                break
            curr.next = node
            node.next = nxt
            curr = nxt

# fix the tail