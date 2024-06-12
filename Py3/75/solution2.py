class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0, 0, 0]

        for num in nums:
            count[num] += 1

        nums.clear()
        
        nums.extend([0] * count[0])
        nums.extend([1] * count[1])
        nums.extend([2] * count[2])
