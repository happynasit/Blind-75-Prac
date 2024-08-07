class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        # this is the hash table method, it gives us O(n) amount of time
        dict_nums = dict()

        for i in nums:
            if i in dict_nums:
                dict_nums[i] += 1
            else:
                dict_nums[i] = 1
        
        for i in dict_nums:
            if dict_nums[i] == 1:
                return i
        """

        # this it the method where we use bits
        answer = 0
        for num in nums:
            answer ^= num
        return answer
