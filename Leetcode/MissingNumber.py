class solution:
    def missingnumber(self, nums: list[int]) -> int:
        i, n = 0, len(nums)
        while i < n:
            j = nums[i]
            if nums[i] < n and nums[i] != nums[j]