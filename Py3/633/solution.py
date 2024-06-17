class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(math.sqrt(c))

        while a <= b:
            currentSum = a * a + b * b
            if currentSum == c:
                return True
            elif currentSum < c:
                a += 1
            else:
                b -= 1

        return False
