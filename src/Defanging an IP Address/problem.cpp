class Solution {
public:
    string defangIPaddr(string address) {
        string defangedIPadd = "";
        for(int i = 0; i < address.length(); i++) {
            if(address.at(i) == '.') {
                defangedIPadd += '[';
                defangedIPadd += '.';
                defangedIPadd += ']';
            }
            else {
                defangedIPadd += address.at(i);
            }
        }
        return defangedIPadd;
    }
};
