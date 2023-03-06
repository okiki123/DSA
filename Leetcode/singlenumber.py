class solution:
    def singlenumber(self, nums:list[int]) -> int:
        res = 0
        for n in nums:
            res = res ^ n
        return res