"""
There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.
"""

def findMinArrowShots(points):
    if not points:
        return 0
    points.sort(key=lambda x: x[1])
    count = 1

    end = points[0][1]
    for i in range(1, len(points)):
        if points[i][0] > end:
            count += 1
            end = points[i][1]
    return count

print(findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))

