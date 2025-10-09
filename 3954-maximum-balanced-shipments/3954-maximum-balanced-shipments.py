from typing import List

class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        n = len(weight)
        count = 0
        start = 0
        while start < n - 1:
            curr_max = weight[start]
            i = start + 1
            formed = False
            while i < n:
                if curr_max > weight[i]:
                    count += 1
                    start = i + 1
                    formed = True
                    break
                curr_max = max(curr_max, weight[i])
                i += 1
            if not formed:
                break
        return count