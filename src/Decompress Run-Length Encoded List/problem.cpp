class Solution {
public:
    vector<int> decompressRLElist(vector<int>& nums) {
        int frequency;
        int value;
        int count = 0;
        vector<int> decompressedList;
        for(int i = 0; i < nums.size(); i+=2) {
            frequency = nums[i];
            value = nums[i + 1];
            for(int j = 1; j <= frequency; j++) {
                decompressedList.push_back(value);
            }
        }
        return decompressedList;
    }
};
