class ZigzagIterator {
public:
    ZigzagIterator(vector<int> &v1, vector<int> &v2) {
        this->v1 = v1;
        this->v2 = v2;
        idx1 = 0;
        idx2 = 0;
        flag = false;
    }

    int next() {
        if(idx1 >= v1.size())
            return v2[idx2++];
        if(idx2 >= v2.size())
            return v1[idx1++];
        flag = !flag;
        return flag ?  v1[idx1++] : v2[idx2++];
    }

    bool hasNext() {
        return idx1 < v1.size() || idx2 < v2.size();
    }

private:
    int idx1;
    int idx2;
    vector<int> v1;
    vector<int> v2;
    bool flag;
};

/**
 * Your ZigzagIterator object will be instantiated and called as such:
 * ZigzagIterator i(v1, v2);
 * while (i.hasNext()) cout << i.next();
 */