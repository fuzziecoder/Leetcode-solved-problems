class Solution(object):
    def kConcatenationMaxSum(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7

        def kadane(nums):
            max_sum = curr = 0
            for num in nums:
                curr = max(0, curr + num)
                max_sum = max(max_sum, curr)
            return max_sum

        max_single = kadane(arr)
        if k == 1:
            return max_single % MOD

        total_sum = sum(arr)
        double_kadane = kadane(arr * 2)

        if total_sum > 0:
            return (double_kadane + (k - 2) * total_sum) % MOD
        else:
            return double_kadane % MOD