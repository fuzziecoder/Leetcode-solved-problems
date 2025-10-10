class Solution(object):
    def maximumValueSum(self, nums, k, edges):
        """
        :type nums: List[int]
        :type k: int
        :type edges: List[List[int]]
        :rtype: int
        """
        l1 = list(map(lambda x, k=k: (x ^ k, 1) if (x ^ k) > x else (x, 0), nums))

        sum_ = sum(list(map(lambda x: x[0], l1)))

        val_cnt = len(list(filter(lambda x: x[1], l1)))

        l3 = list(map(lambda x, k=k: (x ^ k) -x if (x ^ k) > x else x -(x^k) , nums))

        return sum_ if val_cnt % 2== 0  else sum_ - min(l3)
        