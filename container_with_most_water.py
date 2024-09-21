"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.
"""

def max_area(height):
    i,j = 0,1
    area = -1
    for i in range(len(height)):
        for j in range(1,len(height)):
            A = min(height[i],height[j])*(j-i)
            if area<A:
                area = A

    return area
    
print(max_area([1,1]))


# From GPT

def max_area(height):
    left = 0
    right = len(height) - 1
    max_water = 0
    
    while left < right:
        # Calculate the width between the two lines
        width = right - left
        
        # Calculate the height of the container (minimum of the two heights)
        h = min(height[left], height[right])
        
        # Calculate the current area
        current_water = h * width
        
        # Update the maximum area found
        max_water = max(max_water, current_water)
        
        # Move the pointer pointing to the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
            
    return max_water

