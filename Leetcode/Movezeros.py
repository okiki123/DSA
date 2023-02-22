class solution:
    def moveZeros(self, nums:list) -> list:
        prev_idx = 0
        for i in range(len(nums)):
            hold = nums[prev_idx]
            nums[prev_idx] = nums[i]
            nums[i] = hold
            prev_idx += 1
