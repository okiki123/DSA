class solution:
    def twosum(self, nums:list[int], target:int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            x = target - nums[i]
            if x in hashmap:
                return [map[x], i]
            else:
                hashmap[nums[i]] = i
        return []
        
