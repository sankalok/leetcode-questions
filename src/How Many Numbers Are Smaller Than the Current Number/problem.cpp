class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        vector<int> smallerNums(nums.size(), 0);
        int count = 0;
        for(int i = 0; i < nums.size(); i++) {
            for(int j = 0; j < nums.size(); j++) {
                if(i != j) {
                    if(nums[i] > nums[j]) {
                        count += 1;
                    }
                }
            }
            smallerNums[i] = count;
            count = 0;
        }
        return smallerNums;
    }
};
