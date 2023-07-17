class solution:
    def productExceptSelf(self, nums:list[int]) -> list[int]:
        sol = [1] * len(nums)
        pre =  1
        post = 1
        for i in range(len(nums)):
            sol[i] *= pre
            pre *= nums[i]
            