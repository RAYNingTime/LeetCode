class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def process(s, first, second, points):
            stack = []
            score = 0
            for char in s:
                if char == second and stack and stack[-1] == first:
                    stack.pop()
                    score += points
                else:
                    stack.append(char)
            return ''.join(stack), score

        if x > y:
            remaining, score = process(s, 'a', 'b', x)
            _, additional_score = process(remaining, 'b', 'a', y)
        else:
            remaining, score = process(s, 'b', 'a', y)
            _, additional_score = process(remaining, 'a', 'b', x)

        return score + additional_score
