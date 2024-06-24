class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        isFlipped = [0] * n
        flipCount = 0
        result = 0

        for i in range(n):
            if i >= k:
                flipCount ^= isFlipped[i - k]
            
            if (nums[i] ^ flipCount) == 0:
                if i + k > n:
                    return -1
                
                isFlipped[i] = 1
                flipCount ^= 1
                result += 1
        
        return result
