class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        positions = dict()
        for row in range(len(matrix)):
            for column in range(len(matrix[row])):
                if matrix[row][column] == 0:
                    # The entire row becomes 0
                    #matrix[row] = [0 for i in range(len(matrix[row]))]
                    if row in positions:
                        positions[row].append(column)
                    else:
                        positions[row] = [column]
        print(positions)

        for row in positions.keys():
            matrix[row] = [0 for i in range(len(matrix[row]))]

        for columns in positions.values():
            for column in columns:
                for r in range(len(matrix)):
                    matrix[r][column] = 0
        print(matrix)
