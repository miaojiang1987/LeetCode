class RandomizedCollection {
public:
    /** Initialize your data structure here. */
    RandomizedCollection() {
        
    }
    
    /** Inserts a value to the collection. Returns true if the collection did not already contain the specified element. */
    bool insert(int val) {
        bool ret = cache.find(val) == cache.end();
        cache[val].push_back(list.size());
        list.push_back(val);
        //cout << "inserted" << endl;
        return ret;
    }
    
    /** Removes a value from the collection. Returns true if the collection contained the specified element. */
    bool remove(int val) {
        bool ret = cache.find(val) != cache.end();
        if(!ret)
            return ret;
        int cur = cache[val].back();
        //cout << "cur=" << cur << endl;
        if(cur != list.size()-1) {
            swap(list[cur], list.back());
            cache[list[cur]].erase(find(cache[list[cur]].begin(), cache[list[cur]].end(), list.size()-1));
            cache[list[cur]].push_back(cur);
        }
        cache[val].erase(find(cache[val].begin(), cache[val].end(), cur));
        if(cache[val].empty())
            cache.erase(val);
        list.pop_back();
        return ret;
    }
    
    /** Get a random element from the collection. */
    int getRandom() {
        return list[rand() % list.size()];
    }
private:
    vector<int> list;
    unordered_map<int, vector<int>> cache;
};

/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * RandomizedCollection obj = new RandomizedCollection();
 * bool param_1 = obj.insert(val);
 * bool param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */