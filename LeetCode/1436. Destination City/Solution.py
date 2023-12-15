class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        destinations = {path[0]: path[1] for path in paths}

        currentCity = paths[0][0]
        while currentCity in destinations:
            currentCity = destinations[currentCity]

        return currentCity
