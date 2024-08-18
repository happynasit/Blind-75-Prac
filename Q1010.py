class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0

        for i in range(len(time) - 1):
            j = i + 1

            while j < len(time):
                if (time[i] + time[j]) % 60 == 0:
                    count += 1
                j = j + 1
        return(count)
