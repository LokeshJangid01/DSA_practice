"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards come back.

Return the minimum integer k such that Koko can eat all the bananas within h hours.
"""

def minEatingSpeed(piles, h):
    left, right = 1, max(piles)
    while left < right:
        mid = (left + right) // 2
        if sum((pile + mid - 1) // mid for pile in piles) > h:
            left = mid + 1
        else:
            right = mid
    return left # or right, since both will be equal

print(minEatingSpeed([3,6,7,11], 8))

