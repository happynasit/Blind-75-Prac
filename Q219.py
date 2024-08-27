class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        print(nums)

        if len(nums) == 1:
            return False
            
        locations = dict()
        for i in range(len(nums)):
            if nums[i] in locations:
                locations[nums[i]].append(i)
            else:
                locations[nums[i]] = [i]

        for vals in locations.values():
            if len(vals) > 1:
                max_val = max(vals)
                vals.remove(max_val)
                if abs(max_val - max(vals)) <= k:
                    return True
                    break
                
        return False
