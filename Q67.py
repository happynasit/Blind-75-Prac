class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Given two binary strings a and b, return their sum as a binary string.
        """
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
        """
        len_a = len(a)
        len_b = len(b)

        if len_a > len_b:
            difference = len_a - len_b
            empty_zero = ''
            for _ in range(difference):
                empty_zero += '0'
            b = empty_zero + b

        elif len_b > len_a:
            diff = len_b - len_a
            empty = ''
            for _ in range(diff):
                empty += '0'
            a = empty + a

        print(a)
        print(b)

        # Now we have both values 01 and 10

        i = len(a) - 1
        print(i)
        result = ''
        remainder = '0'
        while i >= 0:
            if (a[i] == '0' and b[i] == '1' and remainder == '0') or (b[i] == '0' and a[i] == '1' and remainder == '0'):
                result = '1' + result
                remainder = '0'
                i = i - 1
            elif (a[i] == '0' and b[i] == '0'):
                result = remainder + result
                remainder = '0'
                i = i - 1
            elif (a[i] == '0' and b[i] == '1' and remainder == '1') or (b[i] == '0' and a[i] == '1' and remainder == '1') or a[i] == '1' and b[i] == '1' and remainder == '0':
                result = '0' + result
                remainder = '1'
                i = i - 1
            elif (a[i] == '1' and b[i] == '1' and remainder == '1'):
                result = '1' + result
                remainder = '1'
                i = i - 1
        result = remainder + result

        return result
