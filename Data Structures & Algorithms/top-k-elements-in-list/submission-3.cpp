class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        
        unordered_map<int, int> freq;
        for(int i : nums) {
            freq[i] += 1;
        }
        vector<vector<int>> counts(nums.size()+1);
        for(pair<int, int> p : freq) {
            counts[p.second].push_back(p.first);
        }

        vector<int> ans;
        for(int i = nums.size(); i >= 0; i--) {
            ans.insert(ans.end(), counts[i].begin(), counts[i].end());
            if(ans.size() == k) return ans;
        }
    }
};
