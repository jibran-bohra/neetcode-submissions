class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]

            best = 1

            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    best = max(best, 1 + dfs(j))

            memo[i] = best
            return best

        max_len = 0

        for i in range(n):
            max_len = max(max_len, dfs(i))

        return max_len