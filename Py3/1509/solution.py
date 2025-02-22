class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        
        nums.sort()
        
        min_diff = float('inf')
        n = len(nums)
        
        min_diff = min(min_diff, nums[n-1] - nums[3])
        min_diff = min(min_diff, nums[n-2] - nums[2])
        min_diff = min(min_diff, nums[n-3] - nums[1])
        min_diff = min(min_diff, nums[n-4] - nums[0])
        
        return min_diff
