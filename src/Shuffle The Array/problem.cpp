class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        vector<int> shuffledVector(2*n, 0);
        int i = 0;
        int j = n;
        int count = 0;
        for(i = 0; i < n; i++, j++)
        {
            shuffledVector[count] = nums[i];
            shuffledVector[count + 1] = nums[j];
            count += 2;
        }
        return shuffledVector;
    }
};
