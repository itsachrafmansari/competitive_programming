import math


class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        rows, cols = len(img), len(img[0])

        # a function that calculates the average for a given cell
        def average(row, col) -> int:
            avg = 0
            cells = 0

            # max(0, row-1) assures we stay above 0, while min(rows, row + 2) assures we never surpass the last row
            for i in range(max(0, row - 1), min(rows, row + 2)):

                # max(0, col-1) assures we stay above 0, while min(cols, col+2) assures we never surpass the last column
                for j in range(max(0, col - 1), min(cols, col + 2)):
                    avg += img[i][j]
                    cells += 1

            return math.floor(avg / cells)

        return [[average(row, col) for col in range(cols)] for row in range(rows)]
