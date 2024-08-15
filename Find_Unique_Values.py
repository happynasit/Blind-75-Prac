
class Solution:
  def findUniqueValues(self, experience: List[int]) -> int:
      experience.sort()

      left = 0
      right = len(experience) - 1
      pairs = []
      averages = []
      while left < right:
          pairs.append((experience[left], experience[right]))
          average = (experience[left] + experience[right])/2
          averages.append(average)
          left += 1
          right -=1

      set_averages = set(averages)
    

      return len(set_averages)
