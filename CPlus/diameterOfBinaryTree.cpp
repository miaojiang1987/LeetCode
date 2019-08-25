class Solution {
private:
    int result=0;
    int dfs(TreeNode* root){
        if (!root){
            return 0;
        }
        int left=dfs(root->left);
        int right=dfs(root->right);
        result=max(result,left+right);
        return 1+max(left,right);
    }
    
public:
    int diameterOfBinaryTree(TreeNode* root) {
        dfs(root);
        return result;
    }
    
    
};