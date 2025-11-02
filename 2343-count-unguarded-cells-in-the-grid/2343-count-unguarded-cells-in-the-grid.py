class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        grid = [[0] * n for _ in range(m)]
        for r, c in walls:
            grid[r][c] = 1
        for r, c in guards:
            grid[r][c] = 1
        for r, c in guards:
            u = r - 1
            while u >= 0 and grid[u][c] != 1:
                grid[u][c] = 2
                u -= 1
            d = r + 1
            while d < m and grid[d][c] != 1:
                grid[d][c] = 2
                d += 1
            l = c - 1
            while l >= 0 and grid[r][l] != 1:
                grid[r][l] = 2
                l -= 1
            ri = c + 1
            while ri < n and grid[r][ri] != 1:
                grid[r][ri] = 2
                ri += 1
        unguarded = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    unguarded += 1
        return unguarded