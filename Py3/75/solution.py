class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0, 0, 0]

        for num in nums:
            count[num] += 1

        nums.clear()
        
        for i in range(count[0]):
            nums.append(0)

        for i in range(count[1]):
            nums.append(1)

        for i in range(count[2]):
            nums.append(2)
        
