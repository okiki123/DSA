class solution:
    def containsDuplicate(self, nums:list[int]) -> bool:
        check = {}
        for i in range(len(nums)):
            if nums[i] not in check:
                check[nums[i]] = i
            else:
                return True
        return False
    
    def containsDuplicate2(self, nums:list[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False



