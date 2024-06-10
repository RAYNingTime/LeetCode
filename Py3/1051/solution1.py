# 38 ms  16.43 MB

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        counter = 0
        sorted_heights = sorted(heights)

        for i in range(len(heights)):
            if sorted_heights[i] != heights[i]:
                counter += 1

        return counter 
