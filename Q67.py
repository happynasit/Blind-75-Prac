class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Given two binary strings a and b, return their sum as a binary string.
        """

        # There are 4 situations to consider:
        #   - 0 + 0 = 0
        #   - 1 + 0 = 1
        #   - 1 + 1 = 1 0
        #   - 1 + 1 + 1 = 1 1

        curr = 0
        sum_string = ''
        maximum_length = max(len(a), len(b))

        a = a.zfill(maximum_length)
        b = b.zfill(maximum_length)

        for index in range(maximum_length -1, -1, -1):
            if int(a[index]) + int(b[index]) + curr == 0:
                sum_string = '0' + sum_string
                curr = 0
            elif int(a[index]) + int(b[index]) + curr == 1:
                sum_string = '1' + sum_string
                curr = 0
            elif int(a[index]) + int(b[index]) + curr == 2:
                sum_string = '0' + sum_string
                curr = 1
            elif int(a[index]) + int(b[index]) + curr == 3:
                sum_string = '1' + sum_string
                curr = 1
        if curr == 1:
            sum_string = '1' + sum_string
        
        return sum_string
