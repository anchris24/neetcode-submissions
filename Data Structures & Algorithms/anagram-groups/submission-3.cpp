class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        
        map<array<int, 26>, vector<string>> freqmap;
        for(string word : strs) {
            array<int, 26> freq = {};
            for(char ch : word) {
                freq[int(ch) - int('a')]++;
            }
            freqmap[freq].push_back(word);
        }

        vector<vector<string>> ans;
        for(pair<array<int, 26>, vector<string>> p : freqmap) 
            ans.push_back(p.second);
        return ans;
    }
};