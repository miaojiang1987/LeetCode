class Solution {
public:
    bool isValidSerialization(string preorder) {
        if(preorder.empty())
            return true;
        vector<bool> values;
        size_t index = 0;
        while(true) {
            size_t next = preorder.find(',', index);
            if(next == string::npos)
                break;
            values.push_back(preorder[next-1] != '#');
            index = next + 1;
        }
        values.push_back(preorder[index] != '#');

        int degree = 1;
        for(bool v: values) {
            degree--;
            if(degree < 0)
                return false;
            if(v)
                degree += 2;
        }
        return degree == 0;
    }
};

