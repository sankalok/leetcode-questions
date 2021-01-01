class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        int count = 0;
        int result;
        for(int i = 0; i < words.size(); i++) {
            result = 0;
            for(int j = 0; j < words[i].length(); j++) {
                for(int k = 0; k < allowed.length(); k++) {
                    if(words[i].at(j) == allowed.at(k)) {
                        result += 1;
                    }
                }
            }
            if(result == words[i].length()) {
                count += 1;
            }
        }
        return count;
    }
};
