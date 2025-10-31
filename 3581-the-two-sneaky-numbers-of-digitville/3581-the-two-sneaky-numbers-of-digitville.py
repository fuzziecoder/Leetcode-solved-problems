from typing import List

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        maxelt = max(nums)
        freq = [0] * (maxelt + 1)
        res = []
        
        for n in nums:
            freq[n] += 1
        
        # Collect numbers that appear exactly twice
        for i in range(len(freq)):
            if freq[i] == 2:
                res.append(i)
        
        return res