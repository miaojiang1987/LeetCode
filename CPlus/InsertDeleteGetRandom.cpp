class RandomizedSet {
public:
    /** Initialize your data structure here. */
    RandomizedSet() {
        
    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int val) {
        if(cache.find(val) != cache.end())
            return false;
        cache[val] = list.size();
        list.push_back(val);
        return true;
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    bool remove(int val) {
        if(cache.find(val) == cache.end())
            return false;
        int cur = cache[val];
        if(cur != list.size()-1) {
            swap(list[cur], list.back());
            cache[list[cur]] = cur;
        }
        cache.erase(val);
        list.pop_back();
        return true;
    }
    
    /** Get a random element from the set. */
    int getRandom() {
        return list[rand() % list.size()];
    }

private:
    vector<int> list;
    unordered_map<int, int> cache;
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * bool param_1 = obj.insert(val);
 * bool param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */