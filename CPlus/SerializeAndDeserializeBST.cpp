/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode *root) {
        string ret;
        shared_ptr<vector<TreeNode *>> cur = make_shared<vector<TreeNode *>>();
        cur->push_back(root);
        while(!cur->empty()) {
            shared_ptr<vector<TreeNode *>> next = make_shared<vector<TreeNode *>>();
            for(TreeNode *n: *cur) {
                if(n == nullptr) {
                    if(!ret.empty())
                        ret.push_back(' ');
                    ret.push_back('#');
                    continue;
                }
                if(!ret.empty())
                    ret.push_back(' ');
                ret.append(to_string(n->val));
                next->push_back(n->left);
                next->push_back(n->right);
            }
            cur = next;
        }
        while(ret.back() == ' ' || ret.back() == '#')
            ret.pop_back();
        //cout << "serialized:" << ret << endl;
        return ret;
    }

    // Decodes your encoded data to tree.
    TreeNode *deserialize(string data) {
        size_t pos = 0;
        TreeNode *root = NextNode(data, pos);
        shared_ptr<vector<TreeNode *>> cur = make_shared<vector<TreeNode *>>();
        cur->push_back(root);
        while(pos<data.size()) {
            shared_ptr<vector<TreeNode *>> next = make_shared<vector<TreeNode *>>();
            for(TreeNode *n: *cur) {
                if(n == nullptr)
                    continue;
                //cout << "n:" << n->val << endl;
                n->left = NextNode(data, pos);
                next->push_back(n->left);
                n->right = NextNode(data, pos);
                next->push_back(n->right);
            }
            cur = next;
        }
        return root;
    }

    inline TreeNode *NextNode(const string &data, size_t &start) {
        if(start >= data.size())
            return nullptr;
        if(data[start] == '#') {
            start += 2;
            return nullptr;
        }
        int val = 0;
        while(start < data.size() && data[start] != ' ') {
            val = val * 10 + (data[start] - '0');
            start++;
        }
        //cout << "start:" << start << " val:" << val << endl; 
        start++;
        return new TreeNode(val);
    }
};


// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));