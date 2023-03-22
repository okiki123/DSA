class solution:
    def containsDuplicate(self, nums:list[int]) -> bool:
        check = {}
        for i in range(len(nums)):
            if nums[i] not in check:
                check[nums[i]] = i
            else:
                return True
        return False