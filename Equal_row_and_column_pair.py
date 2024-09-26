"""
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).
"""

def equalPairs(grid):
    count = 0
    n = len(grid)
    row = [tuple(grid[i]) for i in range(n)]
    col = [tuple(grid[j][i] for j in range(n)) for i in range(n)]
    print(row)
    print(col)

    count = 0
    for r in row:
        for c in col:
            if r == c:
                count += 1
    return count

print(equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))

class Solution:                                
    def equalPairs(self, grid: List[List[int]]) -> int:

        tpse = Counter(zip(*grid))                  # <-- determine the transpose
                                                    #     and hash the rows

        grid = Counter(map(tuple,grid))             # <-- hash the rows of grid. (Note the tuple-map, so
                                                    #     we can compare apples w/ apples in next step.)

        return  sum(tpse[t]*grid[t] for t in tpse)  # <-- compute the number of identical pairs
                