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
    vector<vector<int>> verticalOrder(TreeNode *root) {
        unordered_map<int, vector<pair<TreeNode *, int>>> levelMap;
        verticalOrder(root, levelMap, 0, 0);
        vector<int> levels;
        for(auto it=levelMap.begin(); it!=levelMap.end(); it++)
            levels.push_back(it->first);
        sort(levels.begin(), levels.end());
        vector<vector<int>> ret;
        for(int level: levels) {
            vector<int> cur;
            sort(levelMap[level].begin(), levelMap[level].end(), Solution::NodeComparator);
            for(auto m: levelMap[level])
                cur.push_back(m.first->val);
            ret.push_back(cur);
        }
        return ret;
    }
    void verticalOrder(TreeNode *root, unordered_map<int, vector<pair<TreeNode *, int>>> &levelMap, int level, int depth) {
        if(root == nullptr)
            return;
        levelMap[level].emplace_back(root, depth);
        if(root->left != nullptr)
            verticalOrder(root->left, levelMap, level-1, depth+1);
        if(root->right != nullptr)
            verticalOrder(root->right, levelMap, level+1, depth+1);
    }

private:
    static bool NodeComparator(const pair<TreeNode *, int> &n1, const pair<TreeNode *, int> &n2) {
        return n1.second < n2.second;
    }
};