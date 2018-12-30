/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
//LowestCommonAncestorOfABinarySearchTree
class Solution {
public:
    TreeNode *lowestCommonAncestor(TreeNode *root, TreeNode *p, TreeNode *q) {
        if(root == nullptr)
            return root;
        if(root == p || root == q)
            return root;

        TreeNode *cur = root;
        while(true) {
            //cout << cur->val << endl;
            if(cur->val < p->val && cur->val < q->val) {
                cur = cur->right;
            }
            else if(cur->val > p->val && cur->val > q->val) {
                cur = cur->left;
            }
            else {
                break;
            }
        }
        return cur;
    }
};

