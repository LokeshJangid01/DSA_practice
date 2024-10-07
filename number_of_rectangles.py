"""
You are given an array rectangles where rectangles[i] = [li, wi] represents the ith rectangle of length li and width wi.

You can cut the ith rectangle to form a square with a side length of k if both k <= li and k <= wi. For example, if you have a rectangle [4,6], you can cut it to get a square with a side length of at most 4.

Let maxLen be the side length of the largest square you can obtain from any of the given rectangles.

Return the number of rectangles that can make a square with a side length of maxLen.

"""


def countGoodRectangles(rectangles):
    max_len = 0
    count = 0
    
    for length, width in rectangles:
        square_side = min(length, width)
        
        if square_side > max_len:
            max_len = square_side
            count = 1
        elif square_side == max_len:
            count += 1
    
    return count

# Example usage
rectangles = [[5,8],[3,9],[5,12],[16,5]]
result = countGoodRectangles(rectangles)
print(f"Number of rectangles that can make a square with the largest side length: {result}")
