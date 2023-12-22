class Solution:
    def checkStraightLine(self, coors: List[List[int]]) -> bool:
        # Is the slope vertical ?
        if coors[0][0] == coors[1][0]:
            for coor in coors:
                if coor[0] != coors[0][0]:
                    return False

        # Is the slope horizontal ?
        elif coors[0][1] == coors[1][1]:
            for coor in coors:
                if coor[1] != coors[0][1]:
                    return False

        # Else the slope is a normal line
        else:
            # the equation of a line is Ax + B = y. So, let's find A and B

            # A = dy / dx = (coors[0][1] - coors[1][1]) / (coors[0][0] - coors[1][0])
            A = (coors[0][1] - coors[1][1]) / (coors[0][0] - coors[1][0])

            # B = y - AX
            B = coors[0][1] - A * coors[0][0]

            for coor in coors[2:]:
                if A * coor[0] + B != coor[1]:
                    return False

        return True
