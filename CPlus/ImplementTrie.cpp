class Trie {
public:
    /** Initialize your data structure here. */
    Trie() {
        this->root = new TrieNode();
    }
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        TrieNode *cur = this->root;
        for(char ch: word) {
            if(cur->next[ch-'a'] == nullptr)
                cur->next[ch-'a'] = new TrieNode(ch);
            cur = cur->next[ch-'a'];
        }
        cur->IsWord = true;
    }
    
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        TrieNode *cur = this->root;
        for(char ch: word) {
            if(cur->next[ch-'a'] == nullptr)
                return false;
            cur = cur->next[ch-'a'];
        }
        return cur->IsWord;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        TrieNode *cur = this->root;
        for(char ch: prefix) {
            if(cur->next[ch-'a'] == nullptr)
                return false;
            cur = cur->next[ch-'a'];
        }
        return true;
    }

private:
    struct TrieNode {
        char ch;
        bool IsWord;
        TrieNode *next[26];
        TrieNode() {
            fill(next, next+26, nullptr);
            ch = 0;
            IsWord = false;
        }
        TrieNode(char c):TrieNode() {
            ch = c;
        }
    };
    TrieNode *root;

};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * bool param_2 = obj.search(word);
 * bool param_3 = obj.startsWith(prefix);
 */