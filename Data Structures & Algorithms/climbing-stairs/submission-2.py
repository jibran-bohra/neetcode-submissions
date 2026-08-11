class Solution:
    def climbStairs(self, n: int) -> int:
        memo = dict()

        def fib(n):
            if n in memo:
                return memo[n]
            
            if n<2:
                result = n
            else:
                result = fib(n-1) + fib(n-2)
            
            memo[n] = result

            return result
        
        return fib(n+1)