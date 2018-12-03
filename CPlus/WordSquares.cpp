class Solution {
public:
    Solution() {
        this->root = new TrieNode();    
    }
    
    vector<vector<string>> wordSquares(vector<string> &words) {
        vector<vector<int>> sol;
        vector<int> cur;
        
        wordSquares(words, cur, sol);
        vector<vector<string>> ret;
        for(auto il: sol) {
            vector<string> sl(il.size());
            transform(il.begin(), il.end(), sl.begin(), [words](int i) {return words[i];});
            ret.push_back(sl);
        }
        return ret;
    }

    void wordSquares(const vector<string> &words, vector<int> &cur, vector<vector<int>> &sol) {
        if(cur.size() == words[0].size()) {
            sol.push_back(cur);
            return;
        }
        TrieNode *node = this->root;
        size_t ch = cur.size();
        for(int d: cur) {
             node = node->next[words[d][ch]-'a'];
        }
        for(int i: node->indices) {
            cur.push_back(i);
            wordSquares(words, cur, sol);
            cur.pop_back();
        }
    }

    /** Inserts a word into the trie. **/
    void insert(const string &word, int index) {
        TrieNode *cur = this->root;
        cur->indices.push_back(index);
        for(char ch: word) {
            if(cur->next[ch-'a'] == nullptr)
                cur->next[ch-'a'] = new TrieNode(ch);
            cur = cur->next[ch-'a'];
            cur->indices.push_back(index);
        }
    }


private:
    struct TrieNode {
        char ch;
        TrieNode *next[26];
        vector<int> indices;
        TrieNode() {
            fill(next, next+26, nullptr);
            ch = 0;
        }
        TrieNode(char c):TrieNode() {
            ch = c;
        }
    };
    TrieNode *root;
};

