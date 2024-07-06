class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cycle_length = 2 * (n - 1)
        remaining_time = time % cycle_length
        
        if remaining_time < n:
            return remaining_time + 1
        else:
            return n - (remaining_time - n + 1)
