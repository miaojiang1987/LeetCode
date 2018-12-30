/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int kthSmallest(TreeNode *root, int k) {
        vector<int> list;
        kthSmallest(root, k, list);
        return list[k-1];
    }
    
    void kthSmallest(TreeNode *root, int k, vector<int> &list) {
        if(root == nullptr || list.size() >= k)
            return;
        kthSmallest(root->left, k, list);
        list.push_back(root->val);
        kthSmallest(root->right, k, list);
    }
};

