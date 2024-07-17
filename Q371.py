class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        binary_a = str(bin(a)[2:])
        binary_b = str(bin(b)[2:])

        print(binary_a)
        print(binary_b)

        # length of binary numbers to insert 0's in the smaller one
        len_a = len(binary_a)
        len_b = len(binary_b)

        if len_a > len_b:
            difference = len_a - len_b
            empty_zero = ''
            for _ in range(difference):
                empty_zero += '0'
            binary_b = empty_zero + binary_b

        elif len_b > len_a:
            diff = len_b - len_a
            empty = ''
            for _ in range(diff):
                empty += '0'
            binary_a = empty + binary_a

        print(binary_a)
        print(binary_b)

        # Now we have both values 01 and 10

        i = len(binary_a) - 1
        print(i)
        result = ''
        remainder = '0'
        while i >= 0:
            if (binary_a[i] == '0' and binary_b[i] == '1' and remainder == '0') or (binary_b[i] == '0' and binary_a[i] == '1' and remainder == '0'):
                result = '1' + result
                remainder = '0'
                i = i - 1
            elif (binary_a[i] == '0' and binary_b[i] == '0'):
                result = remainder + result
                remainder = '0'
                i = i - 1
            elif (binary_a[i] == '0' and binary_b[i] == '1' and remainder == '1') or (binary_b[i] == '0' and binary_a[i] == '1' and remainder == '1') or binary_a[i] == '1' and binary_b[i] == '1' and remainder == '0':
                result = '0' + result
                remainder = '1'
                i = i - 1
            elif (binary_a[i] == '1' and binary_b[i] == '1' and remainder == '1'):
                result = '1' + result
                remainder = '1'
                i = i - 1
        result = remainder + result
    
        print(result)
        decimal = int(result, 2)
        return(decimal)
        """
