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
    void Traversal(TreeNode* root, vector<int> &nodes) {
        if(root != NULL) {
            nodes.push_back(root->val);
            Traversal(root->left, nodes);
            Traversal(root->right, nodes);
        }
    }
    int rangeSumBST(TreeNode* root, int low, int high) {
        vector<int> nodes;
        Traversal(root, nodes);
        int range = 0;
        for(int i = 0; i < nodes.size(); i++) {
            if(nodes[i] >= low && nodes[i] <= high) {
                range += nodes[i];
            }
        }
        return range;
    }
};
