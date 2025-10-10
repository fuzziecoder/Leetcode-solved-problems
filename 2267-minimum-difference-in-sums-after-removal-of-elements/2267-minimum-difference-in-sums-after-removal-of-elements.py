import heapq

class Solution(object):
    def minimumDifference(self, nums):
        # Step 1: Divide nums into three equal parts
        n = len(nums) // 3

        # ---------- LEFT PART ----------
        # We use a max-heap (simulated using negative values) to maintain the n smallest elements (in terms of largest negatives).
        left_heap = [-a for a in nums[0:n]]  # First n elements
        left_sum = sum(nums[0:n])           # Initial sum of left part
        left_sums = [left_sum]              # Store cumulative minimal sums
        heapq.heapify(left_heap)            # Convert to heap (max-heap via negation)

        # Process elements from index n to 2n - expand left window to find minimal n-element sum
        for i in range(n, 2 * n):
            heapq.heappush(left_heap, -nums[i])      # Add new element (negated)
            left_sum += nums[i]                      # Add to sum
            left_sum -= -heapq.heappop(left_heap)    # Remove largest (least negative) element
            left_sums.append(left_sum)               # Append current minimal left sum

        # ---------- RIGHT PART ----------
        # Use a min-heap to maintain the n largest elements from the right side
        right_heap = nums[2 * n:3 * n]        # Last n elements
        right_sum = sum(right_heap)          # Initial sum of right part
        right_sums = [right_sum]             # Store cumulative maximal sums
        heapq.heapify(right_heap)            # Convert to min-heap

        # Process elements in reverse from index 2n - 1 down to n
        for i in range(2 * n - 1, n - 1, -1):
            heapq.heappush(right_heap, nums[i])     # Add new element
            right_sum += nums[i]                    # Add to sum
            right_sum -= heapq.heappop(right_heap)  # Remove smallest element to maintain max-n elements
            right_sums.append(right_sum)            # Append current maximal right sum

        right_sums = right_sums[::-1]  # Reverse to align with left_sums indices

        # ---------- Final Step ----------
        # Compare difference of left_sums[i] - right_sums[i] for each possible i (0 to n)
        ans = left_sums[0] - right_sums[0]  # Initialize with first comparison
        for i in range(1, n + 1):
            temp = left_sums[i] - right_sums[i]
            if temp < ans:
                ans = temp

        return ans  # Return the minimum possible difference