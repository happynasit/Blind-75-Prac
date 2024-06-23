def singleNumber(nums: List[int]) -> int:
    """
    Given a non-empty array of integers nums, every element appears twice 
    except for one. Find that single one.
    """
    for i in nums:
        count_n = nums.count(i) 
        if count_n == 1:
            return i
