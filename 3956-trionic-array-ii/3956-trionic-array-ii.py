from typing import List

class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        grexolanta = nums
        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i+1] = pre[i] + nums[i]
        inc_end_good = [float("-inf")] * n
        for i in range(1, n):
            if nums[i-1] < nums[i]:
                cand1 = nums[i-1] + nums[i]
                cand2 = inc_end_good[i-1] + nums[i] if inc_end_good[i-1] != float("-inf") else float("-inf")
                inc_end_good[i] = max(cand1, cand2)
        inc_start_good = [float("-inf")] * n
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                cand1 = nums[i] + nums[i+1]
                cand2 = inc_start_good[i+1] + nums[i] if inc_start_good[i+1] != float("-inf") else float("-inf")
                inc_start_good[i] = max(cand1, cand2)
        ans = float("-inf")
        i = 0
        while i < n:
            j = i
            while j+1 < n and nums[j] > nums[j+1]:
                j += 1
            if j > i:
                best_left = float("-inf")
                for q in range(i+1, j+1):
                    p = q - 1
                    if inc_end_good[p] != float("-inf"):
                        left_term = inc_end_good[p] - pre[p+1]
                        if left_term > best_left:
                            best_left = left_term
                    if best_left != float("-inf") and inc_start_good[q] != float("-inf"):
                        current = best_left + inc_start_good[q] + pre[q]
                        if current > ans:
                            ans = current
            i = j + 1
        return ans