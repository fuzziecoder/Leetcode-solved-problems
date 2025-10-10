class Solution(object):
    def maxCoins(self, nums):
        nums = [1] + nums + [1]  
        dp = [[0] * len(nums) for _ in nums]  
        def search(i, j):
            if j - i < 2: return 0
            if dp[i][j] > 0: return dp[i][j] 
            for k in range(i + 1, j):
                dp[i][j] = max(dp[i][j], search(i, k) + search(k, j) + nums[i] * nums[k] * nums[j])
            return dp[i][j]
        return search(0, len(nums) - 1)