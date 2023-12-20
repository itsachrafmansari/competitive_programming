class Solution {
public:
    int buyChoco(vector<int>& prices, int money) {
        int firstMin = 101, secondMin = 101;

        for (int i = 0; i < prices.size(); i++) {
            if (prices[i] < firstMin) {
                secondMin = firstMin;
                firstMin = prices[i];
              
            } else if (prices[i] < secondMin) {
                secondMin = prices[i];
            }
        }

        if (money >= firstMin + secondMin) {
            return money - firstMin - secondMin;
        } else {
            return money;
        }

    }
};
