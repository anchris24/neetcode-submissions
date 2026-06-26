class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        if digits == "":
            return []

        combos = []
        def backtrack(dig2, path):
            if dig2 == "":
                combos.append(path)
                return 

            first = int(dig2[0])
            rest = dig2[1:]

            for ch in mapping[first]:
                backtrack(rest, path + ch)
        
        backtrack(digits, "")
        return combos