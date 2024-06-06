class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        leftPoint = 0
        rightPoint = len(nums) - 1

        while leftPoint < rightPoint:
            sumRes = nums[leftPoint] + nums[rightPoint]
            if sumRes == target:
                return [leftPoint + 1, rightPoint + 1]
            elif sumRes < target:
                leftPoint += 1
            else:
                rightPoint -= 1

        return []
