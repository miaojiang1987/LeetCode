class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (!root) return 0;
        queue<TreeNode*> q{{root}};
        int result=0;
        while(!q.empty()){
            ++result;
            for(int i=q.size();i>0;--i){
                TreeNode *t=q.front();
                q.pop();
                if(t->left) q.push(t->left);
                if(t->right) q.push(t->right);
            }

        }
    
        return result;
    }
};