class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rightPoint = len(nums) - 1
        leftPoint = 0

        while True:
            sumRes = nums[rightPoint] + nums[leftPoint]
            if sumRes == target:
                return[leftPoint + 1, rightPoint + 1]
            elif sumRes > target:
                rightPoint -= 1
            elif sumRes < target:
                leftPoint += 1
