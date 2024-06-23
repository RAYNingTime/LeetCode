class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_deque = deque()
        max_deque = deque()
        start = 0
        max_length = 0
        
        for end in range(len(nums)):
            while min_deque and nums[min_deque[-1]] > nums[end]:
                min_deque.pop()
            while max_deque and nums[max_deque[-1]] < nums[end]:
                max_deque.pop()
            
            min_deque.append(end)
            max_deque.append(end)
            
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                start += 1
                if min_deque[0] < start:
                    min_deque.popleft()
                if max_deque[0] < start:
                    max_deque.popleft()
            
            max_length = max(max_length, end - start + 1)
        
        return max_length
