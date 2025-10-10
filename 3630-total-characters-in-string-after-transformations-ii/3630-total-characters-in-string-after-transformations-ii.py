class Solution(object):
    def lengthAfterTransformations(self, s, t, nums):
        """
        :type s: str
        :type t: int
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        SIZE = 26

        # Step 1: Count the initial occurrences of each character
        count = [0] * SIZE
        for ch in s:
            count[ord(ch) - ord('a')] += 1

        # Step 2: Build the transformation matrix
        T = [[0] * SIZE for _ in range(SIZE)]
        for i in range(SIZE):
            for step in range(1, nums[i] + 1):
                T[i][(i + step) % SIZE] += 1

        # Step 3: Matrix multiplication
        def mat_mult(A, B):
            result = [[0] * SIZE for _ in range(SIZE)]
            for i in range(SIZE):
                for k in range(SIZE):
                    if A[i][k]:
                        for j in range(SIZE):
                            result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % MOD
            return result

        # Step 4: Matrix exponentiation
        def mat_pow(matrix, power):
            result = [[int(i == j) for j in range(SIZE)] for i in range(SIZE)]
            while power:
                if power % 2:
                    result = mat_mult(result, matrix)
                matrix = mat_mult(matrix, matrix)
                power //= 2
            return result

        T_exp = mat_pow(T, t)

        # Step 5: Multiply count vector with T^t
        final_counts = [0] * SIZE
        for i in range(SIZE):
            for j in range(SIZE):
                final_counts[j] = (final_counts[j] + count[i] * T_exp[i][j]) % MOD

        return sum(final_counts) % MOD