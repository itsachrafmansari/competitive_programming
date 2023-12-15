class Solution {
public:
    string destCity(vector<vector<string>>& paths) {
        unordered_map<string, string> destinations;
        
        for (int i = 0; i < paths.size(); i++) {
            destinations.insert({paths[i][0], paths[i][1]});
        }

        string currentCity = paths[0][0];

        while (destinations.find(currentCity) != destinations.end()) {
            currentCity = destinations[currentCity];
        };
        
        return currentCity;
    }
};
