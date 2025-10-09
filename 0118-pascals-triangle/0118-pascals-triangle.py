class Solution:
    def generate(self, numRows):
        triangle = []
        triangle.append([1])

        for row_num in range(1, numRows):
            row = [1]
            prev_row = triangle[row_num - 1]

            for j in range(1, row_num):
                row.append(prev_row[j - 1] + prev_row[j])

            row.append(1)
            triangle.append(row)

        return triangle