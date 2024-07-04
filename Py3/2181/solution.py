# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current_new_list = dummy
        
        current = head.next
        current_sum = 0
        
        while current is not None:
            if current.val == 0:
                # When we encounter a zero, we complete a segment
                if current_sum > 0:
                    current_new_list.next = ListNode(current_sum)
                    current_new_list = current_new_list.next
                    current_sum = 0  # Reset the sum for the next segment
            else:
                # Sum up the values between zeros
                current_sum += current.val
            current = current.next
        
        return dummy.next
