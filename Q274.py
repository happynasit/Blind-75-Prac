class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()

        print(citations)

        for i in range(len(citations)):
            count = 1
            for j in range(i, len(citations)):
                count += 1
                
                if citations[i] == count:
                    return citations[i]
                    break
                
        return 1
