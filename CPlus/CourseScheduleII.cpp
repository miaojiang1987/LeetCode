class Solution {
    
private
    struct AdjList {
        vectorbool in;
        vectorbool out;
        int inCount;
        int outCount;
        AdjList(int n) {
            in.resize(n);
            out.resize(n);
            inCount = 0;
            outCount = 0;
        }
        void add(bool incoming, int i) {
            if(incoming && !in[i]) {
                in[i] = true;
                inCount++;
            }
            else if(!incoming && !out[i]) {
                out[i] = true;
                outCount++;
            }
        }
        void remove(bool incoming, int i) {
            if(incoming && in[i]) {
                in[i] = false;
                inCount--;
            }
            else if(!incoming && !out[i]) {
                out[i] = false;
                outCount--;
            }
        }
    };
    
public
    vectorint findOrder(int numCourses, vectorpairint, int &prerequisites) {
        if(numCourses = 0)
            return vectorint();
        
        unordered_mapint, unique_ptrAdjList graph;
        for(int k=0; knumCourses; k++)
            graph[k] = make_uniqueAdjList(numCourses);
        for(auto &edge prerequisites) {
            graph[edge.second]-add(false, edge.first);
            graph[edge.first]-add(true, edge.second);
        }
        
        vectorint ret = tsort(graph, numCourses);
        return ret;
    }
    
    vectorint tsort(unordered_mapint, unique_ptrAdjList &graph, int numCourses) {
        vectorint ret;
        vectorint st;
        for(auto it=graph.begin(); it!=graph.end(); it++) {
            if(it-second-inCount == 0)
                st.push_back(it-first);
        }
        while(!st.empty()) {
            int cur = st.back(); st.pop_back();
            for(int i=0; igraph[cur]-out.size(); i++) {
                if(!graph[cur]-out[i])
                    continue;
                graph[i]-remove(true, cur);
                if(graph[i]-inCount == 0)
                    st.push_back(i);
            }
            graph[cur]-out = vectorbool(numCourses);
            graph[cur]-outCount = 0;
            ret.push_back(cur);
        }
        for(auto it=graph.begin(); it!=graph.end(); it++) {
            if(!(it-second-outCount==0 && it-second-inCount==0))
                return vectorint();
        }
        return ret;
    }
    
};

