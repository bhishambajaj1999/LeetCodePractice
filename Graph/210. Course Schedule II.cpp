class Solution {
public:
    
    void dfs(int i, vector<int> &col, bool &cycle, vector<vector<int>> &nodes, vector<int> &top) {
        if(col[i] == 1) {
            cycle = true;
            return;
        }
        
        if(col[i] == 2) {
            return;
        }
        
        col[i] = 1;
        
        for(auto j:nodes[i]) {
            dfs(j, col, cycle, nodes, top);
        }
        
        col[i] = 2;
        top.push_back(i);
    }
    
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> nodes;
        vector<int> top;
        nodes.resize(numCourses);
        
        vector<int> col(numCourses, 0);
        bool cycle = false;
        
        for(auto i:prerequisites) {
            nodes[i[1]].push_back(i[0]);
        }
        
        for(int i = 0; i < numCourses; i++) {
            if(cycle) return {};
            dfs(i, col, cycle, nodes, top);
        }
        
        if(cycle) return {};
        
        std::reverse(top.begin(), top.end());
        return top;
    }
};
