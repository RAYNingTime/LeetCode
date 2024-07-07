class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        numEmptyBottles = numBottles
        count = numBottles
        while numEmptyBottles >= numExchange:
            newBottles = numEmptyBottles // numExchange
            count += newBottles
            numEmptyBottles = numEmptyBottles % numExchange + newBottles
        
        return count
