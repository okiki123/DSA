class solution:
    def meetingrooms(self, intervals: [list[list[int]]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        for i in range(len(intervals)- 1)
