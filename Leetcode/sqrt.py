class solution:
    def sqrt(self, x: int) -> int:
        lo, hi = x
        while lo < hi:
            mid = (lo + hi) // 2
            if mid*mid > hi:
                hi = mid - 1
            elif mid*mid < hi:
                lo = mid + 1
            else:
                return mid
        return hi

