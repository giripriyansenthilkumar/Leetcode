class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x:x[0])
        i=1
        while i<len(intervals):
            if intervals[i-1][0]<=intervals[i][0]<=intervals[i-1][1]:
                curr=intervals.pop(i)
                intervals[i-1][1]=max(intervals[i-1][1],curr[1])
            else:
                i+=1
        return intervals