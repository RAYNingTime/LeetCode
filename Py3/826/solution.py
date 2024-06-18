class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        
        worker.sort()
        
        max_profit = 0
        job_index = 0
        current_max_profit = 0
        
        for ability in worker:
            while job_index < len(jobs) and ability >= jobs[job_index][0]:
                current_max_profit = max(current_max_profit, jobs[job_index][1])
                job_index += 1
            max_profit += current_max_profit
        
        return max_profit
