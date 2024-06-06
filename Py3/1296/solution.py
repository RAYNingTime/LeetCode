class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False 

        card_count = Counter(nums)
        
        min_heap = list(card_count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            first_card = min_heap[0]

            for i in range(k):
                current_card = first_card + i

                if current_card not in card_count:
                    return False

                card_count[current_card] -= 1

                if card_count[current_card] == 0:
                    if current_card != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)
        
        return True
