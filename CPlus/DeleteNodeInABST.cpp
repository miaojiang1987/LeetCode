using namespace std;

class Solution {
public:
    TreeNode *deleteNode(TreeNode *root, int key) {
        if(root == nullptr)
            return nullptr;
        
        if(key < root->val) {
            root->left = deleteNode(root->left, key);
            return root;
        }
            
        if(key > root->val) {
            root->right = deleteNode(root->right, key);
            return root;
        }
            
        if(root->right == nullptr) {
            return root->left;
        }
        else {
            TreeNode *next = root->right;
            while(next->left!=nullptr)
                next = next->left;
            root->val = next->val;
            root->right = deleteNode(root->right, root->val);
            return root;
        }
        
    }
};
