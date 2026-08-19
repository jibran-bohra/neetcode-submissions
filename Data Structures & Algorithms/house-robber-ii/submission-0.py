class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        def rob_range(start, end):
            memo = {}

            def rob_house(i):
                if i > end:
                    return 0

                if i in memo:
                    return memo[i]

                rob_current = nums[i] + rob_house(i + 2)
                skip_current = rob_house(i + 1)

                memo[i] = max(rob_current, skip_current)

                return memo[i]

            return rob_house(start)

        return max(
            rob_range(0, n - 2),
            rob_range(1, n - 1)
        )