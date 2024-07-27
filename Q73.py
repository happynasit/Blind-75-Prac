class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        THE SECOND CODE RUNS FASTER, THAT IS FASTER THAN 83. something percent.
        And its easy to understand also, its just by default assigning the arrays to False, and when the thing is 0, then assign it to true.
        # """
        # rows = []
        # columns = []
        # for row in range(len(matrix)):
        #     for column in range(len(matrix[row])):
        #         if matrix[row][column] == 0:
        #             # The entire row becomes 0
        #             rows.append(row)
        #             columns.append(column)

        # for row in rows:
        #     matrix[row] = [0 for i in range(len(matrix[row]))]

        # for column in columns:
        #     for r in range(len(matrix)):
        #         matrix[r][column] = 0

        # print(matrix)
        rLen = len(matrix)
        cLen = len(matrix[0])
        rows = [False] * rLen
        cols = [False] * cLen
        for r in range(rLen):
            for c in range(cLen): # Traverse through matrix and save rows and cols that must be 0
                if matrix[r][c] == 0:
                    rows[r] = True
                    cols[c] = True

        print(rows)
        print(cols)
        for i, r in enumerate(rows): # iterate through rows that must be 0 and set to 0
            if r:
                for c in range(cLen):
                    matrix[i][c] = 0
        for j, c in enumerate(cols): # iterate through cols that must be 0 and set to 0
            if c:
                for r in range(rLen):
                    matrix[r][j] = 0
