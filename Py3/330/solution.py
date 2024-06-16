class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        index = 0  #current pos
        result = 0  # number of patches
        endRange = 0 # end of range
        numsL = len(nums)

        while endRange < n:
            if index < numsL and nums[index] <= endRange + 1:
                endRange += nums[index]
                index += 1
            else: 
                result += 1
                endRange += endRange + 1

        return result
