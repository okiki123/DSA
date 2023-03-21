#Pairs with Sum Target
class solution:
    def pairwithtargetsum(self, nums:list[int], target:int) -> list:
        start, end = 0, len(nums) - 1
        while start < end:
            sum = nums[start] + nums[end]
            if sum < target:
                start += 1
            elif sum > target:
                end -= 1
            else:
                return [start, end]
        return [-1, -1]
    
#Remove Duplicates