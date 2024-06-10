class Solution:
    def quicksort(self, arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            return self.quicksort(left) + middle + self.quicksort(right)


    def heightChecker(self, heights: List[int]) -> int:
        counter = 0
        sorted_heights = self.quicksort(heights)

        for i in range(len(heights)):
            if sorted_heights[i] != heights[i]:
                counter += 1

        return counter 
