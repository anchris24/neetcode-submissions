class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjlist = defaultdict(set)
        allchars = set()
        for w in words:
            for ch in w:
                allchars.add(ch)
        for i in range(len(words) - 1):
            a, b = words[i], words[i+1]

            id1, id2 = 0, 0
            found = False
            while id1 < len(a) and id2 < len(b):
                if a[id1] == b[id2]:
                    id1 += 1
                    id2 += 1
                    continue
                adjlist[a[id1]].add(b[id2])
                found = True
                break
            if not found and len(b) < len(a):
                return ""
        
        ans = []
        # 0: not visited, 1: curr visiting, 2: finished
        state = {ch : 0 for ch in allchars}

        def dfs(ch):
            if state[ch] == 1:
                return False
            
            if state[ch] == 2:
                return True
            
            state[ch] = 1
            for neighbor in adjlist[ch]:
                if not dfs(neighbor):
                    return False
            
            state[ch] = 2
            ans.append(ch)
            print(state, ans)
            return True
        
        for ch in allchars:
            if state[ch] == 0:
                if not dfs(ch):
                    return ""
                dfs(ch)
        
        return "".join(ans[::-1])

        
