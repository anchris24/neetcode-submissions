class Solution {
public:
    bool isAnagram(string s, string t) {
        
        if(s.size() != t.size()) return false;

        int freqs[26] = {};
        for(char ch : s) freqs[(int(ch - 'a'))]++;
        
        for(char ch : t) freqs[(int(ch - 'a'))]--;

        for(int freq : freqs) {
            if(freq != 0) return false;
        }
        return true;
    }
};
