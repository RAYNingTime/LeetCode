class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def mapped_value(num):
            mapped_num = ''.join(str(mapping[int(digit)]) for digit in str(num))
            return int(mapped_num)
        
        # We use a stable sort, and Python's sort is stable by default.
        nums.sort(key=mapped_value)
        return nums
