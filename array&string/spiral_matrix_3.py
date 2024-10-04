"""""
5. Spiral Matrix III
Medium
Topics
Companies
You start at the cell (rStart, cStart) of an rows x cols grid facing east. The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.

You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.). Eventually, we reach all rows * cols spaces of the grid.

Return an array of coordinates representing the positions of the grid in the order you visited them.

Example 1:
Input: rows = 1, cols = 4, rStart = 0, cStart = 0
Output: [[0,0],[0,1],[0,2],[0,3]]
Example 2:

Input: rows = 5, cols = 6, rStart = 1, cStart = 4
Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]

Constraints:

1 <= rows, cols <= 100
0 <= rStart < rows
0 <= cStart < cols

# TIME
# SPACE
""""



class Solution(object):
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        """
        :type rows: int
        :type cols: int
        :type rStart: int
        :type cStart: int
        :rtype: List[List[int]]
        """
        #guarantee to start inbounds
        # guarantee to atleast be a 1x1 (no empty grid)
        # spiral outwards and in clockwise rotation
        # directions array
        # record all cells we traverse
        # How do we know when we are done?
            # of cells in answer === row * col is when we are done
        # When do we switch directions?
            # start with 1 step
            # increase num of steps per direction when we go left or right

        # right, down, left, up
        DIRECTIONS = ((0,1,), (1,0), (0,-1), (-1, 0))
        results = []
        d = 0
        steps = 0
        r,c = rstart, cstart

        # helper function to check if in bounds
        def _inbound(r,c):
            r_inbound = 0 <= r < rows
            c_inbound = 0 <= c < rows
            return r_inbound and c_inbound

        r = 1
        c = 1
        nr = r + DIRECTIONS[d][0] # => 1 + 0 = 1
        nc = c + DIRECTIONS[d][1] # => 1 + 1 = 1
        # nr, nc = (1,2)

        while len(results) < rows*cols:

        return results
