"""
You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

Implement the SmallestInfiniteSet class:

SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
int popSmallest() Removes and returns the smallest integer contained in the infinite set.
void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.
"""

class SmallestInfiniteSet:

    def __init__(self):
        self.smallest = 1
        self.added = set()

    def popSmallest(self) -> int:
        if self.added:
            return self.added.pop()
        else:
            self.smallest += 1
            return self.smallest - 1

    def addBack(self, num: int) -> None:
        if self.smallest > num:
            self.smallest = num
        self.added.add(num) 


obj = SmallestInfiniteSet()
print(obj.popSmallest())
print(obj.addBack(1))
print(obj.popSmallest())


