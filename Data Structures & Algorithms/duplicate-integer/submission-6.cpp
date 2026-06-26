class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        
        unordered_set<int> hashset;
        for(int i : nums) {
            if(hashset.count(i)) return true;
            hashset.insert(i);
        }
        return false;

    }
};