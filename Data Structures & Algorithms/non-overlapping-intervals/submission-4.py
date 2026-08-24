class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])


        prev = intervals[0]
        count = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] < prev[1]:
                count+=1
                prev[1] = min(prev[1], intervals[i][1])
            else:
                prev = intervals[i]

        return count
            



        