class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        vector<bool> boolCandies(candies.size(), 0);
        for(int i = 0; i < candies.size(); i++) {
            int totalCandy = candies[i] + extraCandies;
            int count = 0;
            for(int j = 0; j < candies.size(); j++)
            {
                if(totalCandy >= candies[j])
                    count += 1;
            }
            if(count == candies.size())
                boolCandies[i] = true;
            else
                boolCandies[i] = false;
        }
        return boolCandies;
    }
};
