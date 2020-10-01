class Solution {
public:
    vector<vector<int>> nodes;
    
    int dfs(vector<int> &informTime, int i) {
        int time = 0;
        for(int j = 0; j < nodes[i].size(); j++) {
            time = max(time, dfs(informTime, nodes[i][j]));
            
        }
        
        return time+informTime[i];
    }
    
    int numOfMinutes(int n, int headID, vector<int>& manager, vector<int>& informTime) {
        nodes.resize(n);
        
        for(int i = 0; i < n; i++) {
            if(manager[i] != -1) {
                nodes[manager[i]].push_back(i);
            }
        }
        
        return dfs(informTime, headID);
    }
};
