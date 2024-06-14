class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()

        moves = 0

        min_unique_value = nums[0]
        
        for num in nums:
            if num < min_unique_value:
                moves += min_unique_value - num
            else:
                min_unique_value = num
            
            min_unique_value += 1
            
        return moves
