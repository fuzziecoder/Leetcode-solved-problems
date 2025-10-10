class Solution:
    def trap(self, height):  # Add 'self' as the first parameter
        # Check if the height list is empty
        if not height:
            return 0  # Return 0 if there are no heights

        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water_trapped = 0

        # Use two pointers to traverse the height array
        while left < right:
            if height[left] <= height[right]:
                if height[left] >= left_max:
                    left_max = height[left]  # Update left_max
                else:
                    water_trapped += left_max - height[left]  # Calculate trapped water
                left += 1  # Move the left pointer to the right
            else:
                if height[right] >= right_max:
                    right_max = height[right]  # Update right_max
                else:
                    water_trapped += right_max - height[right]  # Calculate trapped water
                right -= 1  # Move the right pointer to the left

        return water_trapped  # Return the total trapped water

# Example usage:
solution = Solution()  # Create an instance of the Solution class
height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(solution.trap(height1))  # Output: 6

height2 = [4, 2, 0, 3, 2, 5]
print(solution.trap(height2))  # Output: 9