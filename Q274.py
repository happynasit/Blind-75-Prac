class Solution:
    def hIndex(self, citations: List[int]) -> int:
   
        citations.sort()
        for idx in range(len(citations)):
            if len(citations) - idx <= citations[idx]:
                return len(citations) - idx
        return 0
