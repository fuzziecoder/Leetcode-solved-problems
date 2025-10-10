class Solution(object):
    def subarrayBitwiseORs(self, arr):

        res = set()
        cur = set()
        
        for num in arr:
            next_cur = {num}
            for prev in cur:
                next_cur.add(prev | num)
            cur = next_cur
            res.update(cur)
        
        return len(res)