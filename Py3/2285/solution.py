class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # Calculate the degree of each city
        degree = [0] * n
        for road in roads:
            degree[road[0]] += 1
            degree[road[1]] += 1
        
        # Sort cities by degree
        sorted_cities = sorted(range(n), key=lambda x: degree[x], reverse=True)
        
        # Assign values to the cities based on sorted order
        values = [0] * n
        current_value = n
        for city in sorted_cities:
            values[city] = current_value
            current_value -= 1
        
        # Calculate the total importance
        total_importance = 0
        for road in roads:
            total_importance += values[road[0]] + values[road[1]]
        
        return total_importance
