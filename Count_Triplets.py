class Solution:
  def triplets(self, t: int, d: List[int]) -> int:
    """
    Given an array of n distinct integers, d = [d[0], d[1], ..., d[n-1]], and an integer threshold, t, how many (a, b, c) index 
    triplets exist that satisfy both of the following conditions?

    d[a] < d[b] < d[c]
    d[a] + d[b] + d[c] ≤ t
    """
    d.sort()
      
