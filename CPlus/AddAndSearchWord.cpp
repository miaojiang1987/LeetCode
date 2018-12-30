class WordDictionary {
public:
    /** Initialize your data structure here. */
    WordDictionary() {
        this->root = make_shared<TrieNode>(0);
    }
    
    /** Adds a word into the data structure. */
    void addWord(string word) {
        shared_ptr<TrieNode> cur = root;
        for(char c: word) {
            if(cur->next[c-'a'] == nullptr)
                cur->next[c-'a'] = make_shared<TrieNode>(c);
            cur = cur->next[c-'a'];
        }
        cur->isWord = true;
    }
    
    /** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
    bool search(string word) {
        if(word.empty())
            return this->root->isWord;
        return search(word, 0, this->root);
    }

private:

    struct TrieNode {
        char val;
        bool isWord;
        array<shared_ptr<TrieNode>, 26> next;
        TrieNode(char c) {
            val = c;
            isWord = false;
            fill(next.begin(), next.end(), nullptr);
        }
    };
    
    shared_ptr<TrieNode> root;
    
    bool search(const string &word, int index, shared_ptr<TrieNode> &cur) {
        if(word[index] == '.') {
            if(index == word.size()-1) {
                for(auto n: cur->next) {
                    if(n!=nullptr && n->isWord)
                        return true;
                }
                return false;
            }
            else {
                for(auto n: cur->next) {
                    if(n!=nullptr && search(word, index+1, n))
                        return true;
                }
                return false;
            }
        }
        else {
            if(index == word.size()-1) {
                return cur->next[word[index]-'a']!=nullptr && cur->next[word[index]-'a']->isWord;
            }
            else {
                return cur->next[word[index]-'a']!=nullptr && search(word, index+1, cur->next[word[index]-'a']);
            }
        }
    }
    
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * bool param_2 = obj.search(word);
 */