class Solution {
public:
    string interpret(string command) {
        string result = "";
        for(int i = 0; i < command.length(); i++) {
            if(command.at(i) == 'G') {
                result += 'G';
            }
            else if((i + 1) < command.length()) {
                if(command.at(i) == '(' && command.at(i+1) == ')') {
                    result += 'o';
                    i += 1;
                }
                else
                {
                    result += 'a';
                    result += 'l';
                    i += 3;
                }
            }
        }
        return result;
    }
};
