class solution:
    def maxSubarray(self, nums:list[int]) -> int:
        currSum = 0
        maxSub = nums[0]
        for n in nums:
            if currSum < 0:
                currSum = 0
            currSum += n
            maxSub = max(currSum, maxSub)
        