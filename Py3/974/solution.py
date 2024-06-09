class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        running_mod = 0
        # Array to store the frequency of each possible mod value
        mod_count = [0] * k
        # There's one way to have a sum initially divisible by k (sum = 0)
        mod_count[0] = 1

        for num in nums:
            # Update the running sum modulo k
            running_mod = (running_mod + num) % k

            # Ensure running_mod is non-negative
            if running_mod < 0:
                running_mod += k

            # Increment count by the number of times this mod value has been seen
            count += mod_count[running_mod]

            # Increment the frequency of this mod value
            mod_count[running_mod] += 1

        return count
