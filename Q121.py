class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        creating a set of nums and then comparing both the list and set
        would show whether or not it contains duplicates
        """
        if len(set(nums)) == len(nums):
            # it means that the numbers are distinct
            return False
        else:
            return True
        
