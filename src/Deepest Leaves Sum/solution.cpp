/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    void Traversal(TreeNode* root, vector<int> &nodes, vector<int> &levels, int H) {
        if(root != NULL) {
            nodes.push_back(root->val);
            levels.push_back(H);
            Traversal(root->left, nodes, levels, H+1);
            Traversal(root->right, nodes, levels, H+1);
        }
        else {
            nodes.push_back(0);
            levels.push_back(H);
        }
    }
    int deepestLeavesSum(TreeNode* root) {
        vector<int> nodes;
        vector<int> levels;
        Traversal(root, nodes, levels, 0);
        int max = levels[0];
        for(int i = 1; i < nodes.size(); i++) {
            if(levels[i] > max) {
                max = levels[i];
            }
        }
        max -= 1;
        int sum = 0;
        for(int i = 0; i < nodes.size(); i++) {
            if(levels[i] == max) {
                sum += nodes[i];
            }
        }
        return sum;
    }
};
