def singleNumber(nums: List[int]) -> int:
    """
    https://leetcode.com/problems/single-number/
    
    
    Given a non-empty array of integers nums, every element appears twice 
    except for one. Find that single one.

    You must implement a solution with a linear runtime complexity and 
    use only constant extra space.
    """
    for i in nums:
        count_n = nums.count(i) 
        if count_n == 1:
            return i
