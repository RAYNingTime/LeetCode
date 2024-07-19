class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_row_elements = {min(row) for row in matrix}
    
        max_col_elements = set()
        for col in range(len(matrix[0])):
            max_col_elements.add(max(matrix[row][col] for row in range(len(matrix))))
        
        lucky_numbers = min_row_elements.intersection(max_col_elements)
        
        return list(lucky_numbers)
