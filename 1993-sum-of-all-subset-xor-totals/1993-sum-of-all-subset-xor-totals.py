class Solution:
    def subsetXORSum(self, nums):
        def dfs(index, current_xor):
            if index == len(nums):
                return current_xor  # Return XOR sum of this subset
            
            # Include nums[index] in subset
            include = dfs(index + 1, current_xor ^ nums[index])
            # Exclude nums[index] from subset
            exclude = dfs(index + 1, current_xor)

            return include + exclude  # Sum all XOR values
        
        return dfs(0, 0)