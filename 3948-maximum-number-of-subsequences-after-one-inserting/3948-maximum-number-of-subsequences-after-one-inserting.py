class Solution(object):
    def numOfSubsequences(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)

        # Step 1: Forward pass for L and LC counts
        prefix_L = [0] * (n + 1)
        prefix_LC = [0] * (n + 1)
        count_L = 0
        count_LC = 0
        for i in range(n):
            if s[i] == 'L':
                count_L += 1
            elif s[i] == 'C':
                count_LC += count_L
            prefix_L[i + 1] = count_L
            prefix_LC[i + 1] = count_LC

        # Step 2: Backward pass for T and CT counts
        suffix_T = [0] * (n + 1)
        suffix_CT = [0] * (n + 1)
        count_T = 0
        count_CT = 0
        for i in range(n - 1, -1, -1):
            if s[i] == 'T':
                count_T += 1
            elif s[i] == 'C':
                count_CT += count_T
            suffix_T[i] = count_T
            suffix_CT[i] = count_CT

        # Step 3: Count original LCT subsequences
        original = 0
        count_L = 0
        count_LC = 0
        for ch in s:
            if ch == 'L':
                count_L += 1
            elif ch == 'C':
                count_LC += count_L
            elif ch == 'T':
                original += count_LC

        # Step 4: Try all insertion positions and characters
        max_extra = 0
        for i in range(n + 1):
            # Insert 'L' at i: adds LC+LCT via suffix_CT
            max_extra = max(max_extra, suffix_CT[i])
            # Insert 'C' at i: forms LC with prefix_L and completes LCT with suffix_T
            max_extra = max(max_extra, prefix_L[i] * suffix_T[i])
            # Insert 'T' at i: completes existing LC before
            max_extra = max(max_extra, prefix_LC[i])

        return original + max_extra
