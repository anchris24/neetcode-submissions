class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        combinations = []
        mapping = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8': 'tuv', '9':'wxyz'}

        def combo(path, idx):
            if idx == len(digits):
                combinations.append(path)
                return
            
            curr = digits[idx]
            for ch in mapping[curr]:
                combo(path + ch, idx + 1)
        
        combo("", 0)
        return combinations
