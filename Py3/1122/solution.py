class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        def custom_compare(x):
            if x in arr2:
                # If found, given 0 priority for a position
                return (0, arr2.index(x))
            else:
                # Not found, lower priority
                return (1, x)
        
        return sorted(arr1, key=custom_compare)
