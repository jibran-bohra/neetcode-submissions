class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = {}

        def decode(i):
            # The number of ways to decode the substring starting at index i.
            if i == n:
                return 1

            if s[i] == "0":
                return 0
            
            if i in memo:
                return memo[i]

            one_digit = decode(i+1)
            two_digit = 0

            if i + 1 < n:
                if 26 >= int(s[i:i+2]) >= 10:
                    two_digit = decode(i + 2)

            memo[i] = one_digit + two_digit

            return memo[i]
        
        return decode(0)