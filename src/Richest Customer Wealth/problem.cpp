class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int maxWealth = 0;
        for(int i = 0; i < accounts.size(); i++) {
            int sumWealth = 0;
            for(int j = 0; j < accounts[i].size(); j++) {
                sumWealth += accounts[i][j];
            }
            if(sumWealth >= maxWealth) {
                maxWealth = sumWealth;
            }
        }
        return maxWealth;
    }
};
