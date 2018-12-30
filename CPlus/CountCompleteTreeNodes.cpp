
class Solution {
public:
    int countNodes(TreeNode *root) {
        if(root == nullptr)
            return 0;
        int left = height(root->left);
        int right = height(root->right);
        //cout << left <<"," << right << endl;
        if(left == right) {
            return countNodes(root->right) + (1 << left);
        }
        else {
            return countNodes(root->left) + (1 << right);
        }
    }
    static int(*height)(TreeNode *);
};

int(*Solution::height)(TreeNode *) = [](TreeNode *root) {
    int ret = 0;
    while(root != nullptr) {
        ret++;
        root = root->left;
    }
    return ret;
};


