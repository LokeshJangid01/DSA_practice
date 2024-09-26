"""
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
""" 

def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda x: x[1])
    print(intervals)
    count = 0
    end = float('-inf')
    for interval in intervals:
        if interval[0] >= end:
            end = interval[1]
        else:
            count += 1
    return count

print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))

