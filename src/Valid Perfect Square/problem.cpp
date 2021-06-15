class Solution {
public:
    bool isPerfectSquare(int num) {
        if(num == 1) {
            return true;
        }
        for(long i = 0; i <= num/2; i++) {
            if(i*i == num) {
                return true;
            }
            else if(i*i > num) {
                return false;
            }
        }
        return false;
    }
};
