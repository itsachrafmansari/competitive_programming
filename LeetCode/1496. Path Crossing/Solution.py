class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visitedCoors = {0: {0}}
        currentPoint = [0, 0]

        for direction in path:

            # Update the current point's coordinates after moving
            if direction == "E":
                currentPoint[0] += 1
            elif direction == "W":
                currentPoint[0] -= 1
            elif direction == "N":
                currentPoint[1] += 1
            elif direction == "S":
                currentPoint[1] -= 1

            # Check if the current x coordinates has been visited before
            if currentPoint[0] in visitedCoors:

                # Check if the current x coordinates has been visited before
                if currentPoint[1] in visitedCoors[currentPoint[0]]:
                    return True

                else:
                    visitedCoors[currentPoint[0]].add(currentPoint[1])
            else:
                visitedCoors[currentPoint[0]] = {currentPoint[1]}

        return False
