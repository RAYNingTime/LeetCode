# 17.21 MB Beats 96.14% of users with Python3
# Quite bad in speed tho

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rightPoint = len(nums) - 1
        leftPoint = 0

        while leftPoint != rightPoint:
            rightPoint = len(nums) - 1
            while rightPoint != leftPoint:
                if nums[rightPoint] + nums[leftPoint] == target:
                    return[leftPoint, rightPoint]
                rightPoint -= 1
            leftPoint += 1
