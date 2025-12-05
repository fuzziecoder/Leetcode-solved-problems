class Solution:
    def countPartitions(self, a: List[int]) -> int:
        return (len(a) - 1, 0)[sum(a) & 1]
