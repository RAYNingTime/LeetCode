# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        critical_positions = []
        index = 1
        prev = head
        current = head.next
        
        while current and current.next:
            if (current.val > prev.val and current.val > current.next.val) or \
               (current.val < prev.val and current.val < current.next.val):
                critical_positions.append(index)
            
            prev = current
            current = current.next
            index += 1
        
        if len(critical_positions) < 2:
            return [-1, -1]
        
        min_distance = float('inf')
        for i in range(1, len(critical_positions)):
            min_distance = min(min_distance, critical_positions[i] - critical_positions[i - 1])
        
        max_distance = critical_positions[-1] - critical_positions[0]
        
        return [min_distance, max_distance]
