class Solution(object):
    def fib(self, n):
        memo = {}

        def dfs(n):
            if n <= 1:
                return n
            if n in memo:
                return memo[n]
            memo[n] = dfs(n - 1) + dfs(n - 2)
            return memo[n]

        return dfs(n)

#Time Complexity : O(N)
#Space Complexity : O(N)



