class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

      # making a copy of the matrix and working with this one
        copy = matrix.copy()

      # then looping through
      # in [[1, 2, 3],
      #     [4, 5, 6],
      #     [7, 8, 9]]
    # 1 is matrix[0][0] and 4 is matrix [1][0]
    # that means that matrix[i][j], i is the row and the j is the column
        for i in range(len(copy)):
            sample = []

          # we simply append all the [i][0]'s in one array and then ::-1 to reverse it
            for j in range(len(copy[i])):
                # since its an nxn matrix
                sample.append(copy[j][i])
            print(sample)
            sample = sample[::-1]
            print(sample)

          # since i is the row, we simply reassign it.
            matrix[i] = sample




