class Solution {
public:
    string numberToWords(int num) {
        vector<string> triplets;
        if(num == 0)
            return "Zero";
        constexpr char *tripleNames[] = {"", "Thousand", "Million", "Billion"};
        while(num > 0) {
            triplets.push_back(decodeTriplet(num % 1000));
            num /= 1000;
        }
        string ret;
        while(!triplets.empty()) {
            if(!triplets.back().empty()) {
                if(!ret.empty())
                    ret.push_back(' ');
                ret.append(triplets.back());
                if(triplets.size() > 1)
                    ret.append(" " + string(tripleNames[triplets.size()-1]));
            }
            triplets.pop_back();
        }
        return ret;
    }

private:
    constexpr static char *literals_0_19[20] = {
        "Zero",
        "One",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten",
        "Eleven",
        "Twelve",
        "Thirteen",
        "Fourteen",
        "Fifteen",
        "Sixteen",
        "Seventeen",
        "Eighteen",
        "Nineteen"
    };
    constexpr static char *literals_20_90[10] = {
        "", "", //0, 10
        "Twenty",
        "Thirty",
        "Forty",
        "Fifty",
        "Sixty",
        "Seventy",
        "Eighty",
        "Ninety"
    };

    string decodeTriplet(int num) {
        //0-19, 20-99, 100-99
        string ret;
        if(num >= 100) {
            ret.append(literals_0_19[num/100]);
            ret.append(" Hundred");
        }
        num %= 100;
        if(num == 0) {
            return ret;
        }
        if(num < 20) {
            if(!ret.empty())
                ret.push_back(' ');
            ret.append(literals_0_19[num]);
        }
        else {
            if(!ret.empty())
                ret.push_back(' ');
            ret.append(literals_20_90[num/10]);
            num %= 10;
            if(num > 0) {
                if(!ret.empty())
                    ret.push_back(' ');
                ret.append(literals_0_19[num]);
            }
        }
        return ret;
    }

};

constexpr char *Solution::literals_0_19[20];
constexpr char *Solution::literals_20_90[10];



