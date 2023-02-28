class solution:
    def runningsum(self, nums: List[int]) -> List[int]:
        i = 1
        while i < len(nums):
            nums[i] += nums[i - 1]
            i+=1
        return nums