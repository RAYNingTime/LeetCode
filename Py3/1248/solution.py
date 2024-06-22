class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd_indices = []
        
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                odd_indices.append(i)
        
        if len(odd_indices) < k:
            return 0
        
        count = 0
        
        for i in range(len(odd_indices) - k + 1):
            start = odd_indices[i]
            end = odd_indices[i + k - 1]
            
            if i == 0:
                left_options = start + 1
            else:
                left_options = start - odd_indices[i - 1]
            
            if i + k - 1 == len(odd_indices) - 1:
                right_options = len(nums) - end
            else:
                right_options = odd_indices[i + k] - end
            
            count += left_options * right_options
        
        return count
