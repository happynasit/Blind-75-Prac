class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
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
                print(max_val)
                vals.remove(max_val)
                print(max(vals))
                if abs(max_val - max(vals)) <= k:
                    print(max_val, max(vals))
                    return True
                    break
        print(locations)
        return False
        '''
        # Create hset for storing previous of k elements...
        hset = {}
        # Traverse for all elements of the given array in a for loop...
        for idx in range(len(nums)):
            # If duplicate element is present at distance less than equal to k, return true...
            if nums[idx] in hset and abs(idx - hset[nums[idx]]) <= k:
                return True
            hset[nums[idx]] = idx
        # If no duplicate element is found then return false...
        return False
