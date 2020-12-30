class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        int countJewels = 0;
        for(int i = 0; i < jewels.length(); i++) {
            for(int j = 0; j < stones.length(); j++) {
                if(jewels.at(i) == stones.at(j)) {
                    countJewels += 1;
                }
            }
        }
        return countJewels;
    }
};
