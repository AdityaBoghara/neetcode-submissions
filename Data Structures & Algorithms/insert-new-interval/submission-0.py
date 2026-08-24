class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []


        for i in range(len(intervals)):
            if intervals[i][1] < newInterval[0]:  #current interval ends before newInterval start
                res.append(intervals[i])
                
            elif intervals[i][0] > newInterval[1]:
            #current interval starts after newinterval
                res.append(newInterval)
                return res + intervals[i:]
            
            else: 
                newInterval = [min(intervals[i][0],newInterval[0]), 
                            max(intervals[i][1],newInterval[1])]

        res.append(newInterval)

        return res
        