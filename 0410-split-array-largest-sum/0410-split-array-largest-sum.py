class Solution:
    def splitArray(self, nums, k):
        def canSplit(maxSum):
            subarray_count = 1
            current_sum = 0
            for num in nums:
                if current_sum + num > maxSum:
                    subarray_count += 1
                    current_sum = num
                    if subarray_count > k:
                        return False
                else:
                    current_sum += num
            return True

        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if canSplit(mid):
                right = mid  # Try a smaller maximum sum
            else:
                left = mid + 1  # Increase the allowed sum
        
        return left  # The minimized largest sum
