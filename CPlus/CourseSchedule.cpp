class Solution {
public:
    bool canFinish(int numCourses, vector<pair<int, int>> &prerequisites) {
        map<int, vector<int>> graph;
        vector<int> color(numCourses);

        for(auto &p: prerequisites) {
            graph[p.second].push_back(p.first);
        }

        for(int n=0; n<numCourses; n++) {
            if(color[n] != 2 && isCyclic(n, graph, color,n))
                return false;
        }
        return true;
    }

    bool isCyclic(int n, map<int, vector<int>> &g, vector<int> &color, int start) {
        if(color[start] == 1)
            return true;
        if(color[start] == 2)
            return false;
        
        color[start] = 1;
        for(int n: g[start]) {
            if(color[n] != 2) {
                if(isCyclic(n, g, color, n))
                    return true;
            }
        }
        color[start] = 2;
        return false;
    }
};

