class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        n = len(questions)
        dp = [0] * (n + 1)  # DP array to store the max points at each index

        for i in range(n - 1, -1, -1):  # Traverse the list in reverse
            points, brainpower = questions[i]
            next_index = i + brainpower + 1
            solve = points + (dp[next_index] if next_index < n else 0)
            skip = dp[i + 1]
            dp[i] = max(solve, skip)

        return dp[0]