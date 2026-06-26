class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        unordered_map<int, int> hashmap;
        for(int i = 0; i<nums.size(); i++) {
            int need = target - nums[i];
            if(hashmap.count(need)) {
                return {hashmap[need], i};
            }
            hashmap[nums[i]] = i;
        }
    }
};
