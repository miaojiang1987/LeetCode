class Solution {
public:
    Solution() {
        this->root = make_shared<TrieNode>(0);
    }

    vector<string> findWords(vector<vector<char>> &board, vector<string> &words) {
        vector<string> ret;
        int h = board.size();
        if(h == 0)
            return ret;
        int w = board[0].size();
        if(w == 0)
            return ret;
        vector<vector<bool>> isVisited(h, vector<bool>(w, false));
        for(int i=0; i<words.size(); i++) {
            insert(words[i], i);
        }
        //cout << "inserted" << endl;
        unordered_set<int> sol;
        for(int j=0; j<h; j++)
            for(int i=0; i<w; i++) {
                //cout << "at:" << board[j][i] << endl;
                findWords(board, sol, this->root, j, i, isVisited);
            }

        for(int i: sol)
            ret.push_back(words[i]);
        return ret;
    }


private:
    struct TrieNode {
        char val;
        unique_ptr<int> word;
        array<shared_ptr<TrieNode>, 26> next;
        TrieNode(char c) {
            val = c;
            word = nullptr;
            fill(next.begin(), next.end(), nullptr);
        }
    };

    shared_ptr<TrieNode> root;

    /** Inserts a word into the trie. */
    void insert(const string &word, int index) {
        if(word.empty()) {
            this->root->word = make_unique<int>(index);
            return;
        }
        shared_ptr<TrieNode> cur = root;
        for(char ch: word) {
            if(cur->next[ch-'a'] == nullptr)
                cur->next[ch-'a'] = make_shared<TrieNode>(ch);
            cur = cur->next[ch-'a'];
        }
        cur->word = make_unique<int>(index);
    }

    /** Returns if the word is in the trie. */
    bool search(string word) {
        shared_ptr<TrieNode> cur = root;
        for(char ch: word) {
            if(cur->next[ch-'a'] == nullptr)
                return false;
            cur = cur->next[ch-'a'];
        }
        return cur->word != nullptr;
    }

    void findWords(const vector<vector<char>> &board,
            unordered_set<int> &sol,
            shared_ptr<TrieNode> &cur, //not null
            int y, int x, //not out of bounds
            vector<vector<bool>> &isVisited) {

        shared_ptr<TrieNode> next = cur->next[board[y][x]-'a'];
        if(next == nullptr)
            return;
        if(next->word != nullptr)
            sol.insert(*next->word);

        isVisited[y][x] = true;

        //cout << "next char = " << board[y][x] << endl;

        int h = board.size(), w = board[0].size();
        if(x>0 && !isVisited[y][x-1]) {
            findWords(board, sol, next, y, x-1, isVisited);
        }
        if(x<w-1 && !isVisited[y][x+1]) {
            findWords(board, sol, next, y, x+1, isVisited);
        }
        if(y>0 && !isVisited[y-1][x]) {
            findWords(board, sol, next, y-1, x, isVisited);
        }
        if(y<h-1 && !isVisited[y+1][x]) {
            findWords(board, sol, next, y+1, x, isVisited);
        }
        isVisited[y][x] = false;
    }

};



