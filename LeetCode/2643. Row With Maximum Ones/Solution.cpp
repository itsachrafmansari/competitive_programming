class Solution {
public:
    vector<int> rowAndMaximumOnes(vector<vector<int>>& mat) {
        int maxOnesRowIndex = 0;
        int maxOnes = 0;

        for (int i = 0; i < mat.size(); i++) {
            int currentOnes = count(mat[i].begin(), mat[i].end(), 1);

            if (currentOnes > maxOnes) {
                maxOnes = currentOnes;
                maxOnesRowIndex = i;
            }
        }
        
        return vector<int> {maxOnesRowIndex, maxOnes};
    }
};
