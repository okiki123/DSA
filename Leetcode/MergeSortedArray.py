class solution:
    def mergesortedarrays(self, nums1:list[int], m:int, nums2:list[int], n:int) -> list:
        last = m + n - 1
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
