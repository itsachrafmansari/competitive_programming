class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        
        for (int i = 0; i < grid.size(); i++)
        {
            for (int j = 0; j < grid[0].size(); j++)
            {   
                if (i > 0 || j > 0)
                {
                    grid[i][j] += min(i > 0 ? grid[i-1][j] : 201, j > 0 ? grid[i][j-1] : 201);
                }

            }
            
        }
        
        return grid.back().back();
    }
};
