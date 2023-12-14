class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        def count(l: list[int]):
            meta = {"ones": 0, "zeros": 0}
            
            for num in l:
                if num == 1:
                    meta["ones"] += 1
                elif num == 0:
                    meta["zeros"] += 1
                        
            return meta
        
        rows = [count(row) for row in grid]
        cols = [count([grid[j][i] for j in range(len(grid))]) for i in range(len(grid[0]))]
        
        diff = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                diff[i][j] = rows[i]["ones"] + cols[j]["ones"] - rows[i]["zeros"] - cols[j]["zeros"]
    
        return diff
