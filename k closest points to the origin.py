
"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
"""
def k_closest(points, k):
    # Sort points based on their distance from origin (0, 0)
    sorted_points = sorted(points, key=lambda p: p[0]**2 + p[1]**2)
    # Return the first k points
    return sorted_points[:k]

print(k_closest([[1,3],[-2,2]], 1))
print(k_closest([[3,3],[5,-1],[-2,4]], 2))
