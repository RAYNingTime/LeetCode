class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
    
        always_satisfied = sum(customers[i] for i in range(n) if grumpy[i] == 0)
        

        additional_satisfied = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                additional_satisfied += customers[i]
        
        max_additional_satisfied = additional_satisfied
        
        for i in range(minutes, n):
            if grumpy[i] == 1:
                additional_satisfied += customers[i]
            if grumpy[i - minutes] == 1:
                additional_satisfied -= customers[i - minutes]
            max_additional_satisfied = max(max_additional_satisfied, additional_satisfied)
        
        return always_satisfied + max_additional_satisfied
