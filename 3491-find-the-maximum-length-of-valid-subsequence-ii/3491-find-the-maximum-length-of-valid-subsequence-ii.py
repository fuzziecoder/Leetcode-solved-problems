class Solution(object):
    def maximumLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        dp = [dict() for _ in range(n)]
        ans = 1                   

        for i in range(1, n):
            dpi = {}               
            for j in range(i):
                c = (nums[j] + nums[i]) % k
                new_len = 2

                if c in dp[j]:
                    new_len = dp[j][c] + 1

                if new_len > dpi.get(c, 0):
                    dpi[c] = new_len
                    ans = max(ans, new_len)

            dp[i] = dpi

        return ans