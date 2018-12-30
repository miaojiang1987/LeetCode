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
    vector<int> rightSideView(TreeNode *root) {
        vector<int> ret;
        if(root == nullptr)
            return ret;
        shared_ptr<vector<TreeNode *>> cur = make_shared<vector<TreeNode *>>();
        cur->push_back(root);
        while(!cur->empty()) {
            shared_ptr<vector<TreeNode *>> next = make_shared<vector<TreeNode *>>();
            ret.push_back(cur->back()->val);
            for(TreeNode *n: *cur) {
                if(n->left != nullptr)
                    next->push_back(n->left);
                if(n->right != nullptr)
                    next->push_back(n->right);
            }
            cur = next;
        }
        return ret;
    }
};
