class Solution {
public:
    long long getMaxFunctionValue(vector<int>& adjacencyList, long long k) {
        long long n = adjacencyList.size();
        long long maxFunctionValue = 0; // Initialize the maximum function value.

        // Create two matrices for dynamic programming.
        vector<vector<long long>> parent(n, vector<long long>(40, 0));
        vector<vector<long long>> sum(n, vector<long long>(40, 0));

        // Initialize the base cases for the matrices.
        for (long long i = 0; i < n; i++) {
            parent[i][0] = adjacencyList[i];
            sum[i][0] = adjacencyList[i];
        }

        // Fill in the dynamic programming matrices.
        for (long long i = 1; i < 40; i++) {
            for (long long j = 0; j < n; j++) {
                parent[j][i] = parent[parent[j][i - 1]][i - 1];
                sum[j][i] = sum[j][i - 1] + sum[parent[j][i - 1]][i - 1];
            }
        }

        // Calculate the maximum function value for each element in the adjacency list.
        for (long long i = 0; i < n; i++) {
            long long currentFunctionValue = i; // Initialize the current function value.
            long long currentPosition = i; // Initialize the current position.
            long long shift = 1;

            // Iterate through the binary representation of k.
            for (long long j = 0; j < 40; j++) {
                if (j != 0) shift <<= 1; // Left shift by 1.

                // If the j-th bit of k is set, update the current function value and position.
                if (k & shift) {
                    currentFunctionValue += sum[currentPosition][j];
                    currentPosition = parent[currentPosition][j];
                }
            }

            // Update the maximum function value if the current one is greater.
            maxFunctionValue = max(maxFunctionValue, currentFunctionValue);
        }

        return maxFunctionValue;
    }
};