class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        positions = []
        for row in range(len(matrix)):
            for column in range(len(matrix[row])):
                if matrix[row][column] == 0:
                    # The entire row becomes 0
                    positions.append(column)
                    print(positions)
                    matrix[row] = [0 for i in range(len(matrix[row]))]
        for row in range(len(matrix)):
            for position in positions:
                matrix[row][position] = 0
        print(matrix)
