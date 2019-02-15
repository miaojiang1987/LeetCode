class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result;
        stack<TreeNode*> s;
        TreeNode* p=root;
        while (p||!s.empty()){
            while(p){
                s.push(p);
                p=p->left;
            }
            p=s.top();
            s.pop();
            result.push_back(p->val);
            p=p->right;
        }
        return result;
    }
};