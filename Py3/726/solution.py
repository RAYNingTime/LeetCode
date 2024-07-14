class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [defaultdict(int)]
        i, n = 0, len(formula)
        
        while i < n:
            if formula[i] == '(':
                stack.append(defaultdict(int))
                i += 1
            elif formula[i] == ')':
                top = stack.pop()
                i += 1
                i_start = i
                while i < n and formula[i].isdigit():
                    i += 1
                multiplier = int(formula[i_start:i] or 1)
                for atom, count in top.items():
                    stack[-1][atom] += count * multiplier
            else:
                i_start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                atom = formula[i_start:i]
                i_start = i
                while i < n and formula[i].isdigit():
                    i += 1
                count = int(formula[i_start:i] or 1)
                stack[-1][atom] += count
        
        final_count = stack.pop()
        sorted_atoms = sorted(final_count.items())
        result = []
        for atom, count in sorted_atoms:
            result.append(atom)
            if count > 1:
                result.append(str(count))
        
        return ''.join(result)
