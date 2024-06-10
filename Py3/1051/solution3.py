# 47 ms 16.38 MB

class Solution:
    def merge_sort(self,arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        left_sorted = self.merge_sort(left_half)
        right_sorted = self.merge_sort(right_half)

        return self.merge(left_sorted, right_sorted)

    def merge(self,left, right):
        result = []
        left_index = 0
        right_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1

        result.extend(left[left_index:])
        result.extend(right[right_index:])

        return result


    def heightChecker(self, heights: List[int]) -> int:
        counter = 0
        sorted_heights = self.merge_sort(heights)

        for i in range(len(heights)):
            if sorted_heights[i] != heights[i]:
                counter += 1

        return counter 
