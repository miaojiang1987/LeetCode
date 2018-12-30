class Solution {
public:
    vector<string> findItinerary(vector<pair<string, string>> tickets) {
        map<string, multiset<string>> graph = getGraph(tickets);
        vector<string> sol;
        findItinerary(graph, "JFK", sol);
        reverse(sol.begin(), sol.end());
        return sol;
    }
    
    void findItinerary(map<string, multiset<string>> &graph, const string &start, vector<string> &sol) {
        while(!graph[start].empty()) {
            string next = *graph[start].begin();
            graph[start].erase(graph[start].begin());
            findItinerary(graph, next, sol);
        }
        sol.push_back(start);
    }
    
    map<string, multiset<string>> getGraph(const vector<pair<string, string>> &tickets) {
        map<string, multiset<string>> ret;
        for(auto &p: tickets) 
            ret[p.first].insert(p.second);
        return ret;
    }
};
