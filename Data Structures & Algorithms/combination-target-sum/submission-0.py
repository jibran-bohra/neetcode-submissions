class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        def check_sum(i, current, total):
            if total == target:
                results.append(current.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            current.append(candidates[i])
            check_sum(i, current, total + candidates[i])
            current.pop()
            check_sum(i+1, current, total)

        check_sum(0, [], 0)

        return results
