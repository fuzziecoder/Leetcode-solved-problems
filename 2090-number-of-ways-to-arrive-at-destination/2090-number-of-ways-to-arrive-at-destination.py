import heapq

class Solution:
    def countPaths(self, n, roads):
        MOD = 10**9 + 7
        
        # Step 1: Build the adjacency list safely
        graph = {i: [] for i in range(n)}
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))

        # Step 2: Initialize Dijkstra’s Algorithm
        min_heap = [(0, 0)]  # (time, node)
        shortest_time = [float('inf')] * n
        shortest_time[0] = 0
        ways = [0] * n
        ways[0] = 1

        while min_heap:
            cur_time, node = heapq.heappop(min_heap)

            # Skip processing if this path is outdated
            if cur_time > shortest_time[node]:
                continue  

            for neighbor, travel_time in graph[node]:
                new_time = cur_time + travel_time

                # Found a shorter path
                if new_time < shortest_time[neighbor]:
                    shortest_time[neighbor] = new_time
                    ways[neighbor] = ways[node]  # Reset count
                    heapq.heappush(min_heap, (new_time, neighbor))
                
                # Found another shortest path
                elif new_time == shortest_time[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % MOD

        return ways[n - 1]
sol = Solution()
print(sol.countPaths(7, [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],
                         [3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]])) 
# Expected Output: 4
